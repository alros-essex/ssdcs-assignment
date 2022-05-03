'''Module to manage the database'''

import mysql.connector

from .model import Measure, Experiment, User
from .errors import DbIntegrityError

class StorageConfiguration():
    '''Database configuration'''

    def __init__(self, db_user:str, db_password:str, db_host:str, db_database:str) -> None:
        self._db_user = db_user
        self._db_password = db_password
        self._db_host = db_host
        self._db_database = db_database

    @property
    def user(self):
        '''returns user'''
        return self._db_user

    @property
    def password(self):
        '''returns password'''
        return self._db_password

    @property
    def host(self):
        '''returns hostname'''
        return self._db_host

    @property
    def database(self):
        '''returns db name'''
        return self._db_database

class Storage():
    '''Main component exposing queries'''

    def __init__(self, storage_configuration:StorageConfiguration) -> None:
        self.cnx = mysql.connector.connect(user = storage_configuration.user,
                                           password = storage_configuration.password,
                                           host = storage_configuration.host,
                                           database = storage_configuration.database)

    # Measures

    def read_measure(self, experiment_id:int, page:int, current_user:str):
        '''returns measures'''
        #TODO add pagination
        cur = self._execute('''SELECT ex.NAME as EXP_NAME, me.TIMESTAMP,
                            me.MEASURE_VALUE, mt.NAME as MSR_TYPE
                            FROM MEASURES me, EXPERIMENTS ex, MEASURE_TYPES mt, USER_EXPERIMENTS ue
                            WHERE  me.EXPERIMENT_ID = ex.ID
                            AND mt.ID = me.TYPE
                            AND ue.USER_ID = %(user_id)s
                            AND ue.EXPERIMENT_ID = ex.ID
                            AND ex.ID = %(experiment_id)s
                            ORDER BY TIMESTAMP DESC''',
                            {
                                'experiment_id': experiment_id,
                                'user_id': current_user
                            },
                            for_update = False)
        return [Storage._to_measure(me) for me in cur]

    def insert_measure(self, measure:Measure) -> None:
        '''Inserts a measure'''
        self._execute('''INSERT INTO MEASURES
                      (TYPE, TIMESTAMP, EXPERIMENT_ID, MEASURE_VALUE)
                      VALUES (
                      (SELECT ID FROM MEASURE_TYPES WHERE NAME = %(type)s),
                      FROM_UNIXTIME(%(timestamp)s),
                      (SELECT ID FROM EXPERIMENTS WHERE NAME = %(experiment)s),
                      %(value)s)''',
                      {
                          'type': measure.measure_type,
                          'timestamp': measure.timestamp,
                          'experiment': measure.experiment,
                          'value': measure.value
                      })

    # Experiments

    def read_experiments(self, current_user:int):
        '''Retrieves all experiments visible to the user'''
        cur = self._execute('''SELECT ex.ID, ex.NAME
                            FROM EXPERIMENTS ex, USER_EXPERIMENTS ue, USERS us, ROLES ro
                            WHERE us.ROLE = ro.ID
                            AND us.ID=%(user_id)s
                            AND ro.NAME = 'ADMIN'
                            UNION
                            SELECT ex.ID, ex.NAME
                            FROM EXPERIMENTS ex, USER_EXPERIMENTS ue, USERS us, ROLES ro
                            WHERE us.ROLE = ro.ID
                            AND us.ID=%(user_id)s
                            AND us.ID = ue.USER_ID 
                            AND ex.ID = ue.EXPERIMENT_ID''',
                            { 'user_id': current_user },
                            for_update = False)
        return [Storage._to_experiment(ex) for ex in cur]

    # to be protected with user's check from the caller
    def insert_experiment(self, experiment:Experiment) -> None:
        '''inserts an experiment'''
        self._execute('''INSERT INTO EXPERIMENTS(NAME) VALUES (%(name)s)''',
                      { 'name': experiment.name })

    # to be protected with user's check from the caller
    def read_experiment(self, experiment_id:int) -> Experiment:
        '''returns an experiment given its id'''
        cur = self._execute('''SELECT ex.ID, ex.NAME
                            FROM EXPERIMENTS ex
                            WHERE ex.ID = %(experiment_id)s''',
                            { 'experiment_id': experiment_id },
                            for_update = False)
        experiments = [Storage._to_experiment(ex) for ex in cur]
        return experiments[0] if len(experiments)>0 else None

    # to be protected with user's check from the caller
    def update_experiment(self, experiment:Experiment) -> None:
        self._execute('''UPDATE EXPERIMENTS SET NAME = (%(name)s) WHERE ID=%(id)s''',
                      { 'name': experiment.name, 'id': experiment.experiment_id })

    # Users

    def read_user(self, user_id:str, current_user:str) -> User:
        '''retrieves a user'''
        cur = self._execute('''SELECT us.ID, us.NAME, us.USERNAME, us.EMAIL, ro.NAME AS ROLE
                            FROM USERS us, ROLES ro
                            WHERE us.ROLE = ro.ID
                            AND us.ID = %(user_id)s
                            AND (%(user_id)s = %(requesting_user_id)s OR 
                            (SELECT ro.NAME 
                            FROM USERS us, ROLES ro 
                            WHERE us.ROLE = ro.ID
                            AND us.ID = %(requesting_user_id)s) = 'ADMIN')''',
                            { 'user_id': user_id, 'requesting_user_id': current_user},
                            for_update = False)
        users = [Storage._to_user(u) for u in cur]
        return users[0] if len(users)>0 else None

    def insert_user(self, user:User):
        self._execute('''INSERT INTO USERS(ID, NAME, USERNAME, EMAIL, ROLE)
                      VALUES(%(id)s, %(name)s, %(username)s, %(email)s,
                      (SELECT ID FROM ROLES WHERE NAME = %(role)s))''',
                      {
                          'id': user.user_id,
                          'name': user.name,
                          'username': user.username,
                          'email': user.email,
                          'role': user.role
                      })

    def update_user(self, user:User):
        self._execute('''UPDATE USERS SET
                      NAME = %(name)s,
                      EMAIL = %(email)s,
                      USERNAME = %(username)s
                      WHERE ID = %(id)s''',
                      {
                          'id': user.user_id,
                          'name': user.name,
                          'email': user.email,
                          'username': user.username
                      })

    def read_users(self):
        cur = self._execute('''SELECT us.ID, us.NAME, us.USERNAME, us.EMAIL, ro.NAME
                            FROM USERS us, ROLES ro
                            WHERE us.ROLE = ro.ID''', {}, for_update = False)
        return [Storage._to_user(u) for u in cur]

    def read_users_by_username(self, username:str):
        cur = self._execute('''SELECT us.ID, us.NAME, us.USERNAME, us.EMAIL, ro.NAME
                            FROM USERS us, ROLES ro
                            WHERE us.ROLE = ro.ID AND us.USERNAME = %(username)s''',
                            { 'username': username },
                            for_update = False)
        return [Storage._to_user(u) for u in cur]

    def read_users_by_email(self, email:str):
        cur = self._execute('''SELECT us.ID, us.NAME, us.USERNAME, us.EMAIL, ro.NAME
                            FROM USERS us, ROLES ro
                            WHERE us.ROLE = ro.ID AND us.EMAIL = %(email)s''',
                            { 'email': email },
                            for_update = False)
        return [Storage._to_user(u) for u in cur]

    def user_is_admin(self, user_id:str) -> bool:
        '''true if the user is admin'''
        cur = self._execute('''SELECT ro.NAME = 'ADMIN'
                            FROM USERS us, ROLES ro 
                            WHERE us.ROLE = ro.ID
                            AND us.ID = %(user_id)s''',
                            { 'user_id': user_id },
                            for_update = False)
        return [r[0] for r in cur][0] == 1

    # Scientist/Experiment

    # to be protected with user's check from the caller
    def read_associations(self):
        cur = self._execute('''SELECT us.ID AS USER_ID, us.NAME AS USER_NAME,
                            us.USERNAME AS USER_USERNAME, us.EMAIL AS USER_EMAIL,
                            ro.NAME AS USER_ROLE,
                            ex.ID AS EXPERIMENT_ID, ex.NAME as EXPERIMENT_NAME
                            FROM USER_EXPERIMENTS ue, USERS us, EXPERIMENTS ex,
                            ROLES ro
                            WHERE us.ID = ue.USER_ID
                            AND ex.ID = ue.EXPERIMENT_ID
                            AND ro.ID = us.ROLE''',
                            {}, for_update = False)
        return [Storage._to_association(association) for association in cur]

    # to be protected with user's check from the caller
    def associate_scientist_experiment(self, scientist:int, experiment:int):
        self._execute('''INSERT INTO USER_EXPERIMENTS(USER_ID, EXPERIMENT_ID)
                      VALUES(%(scientist)s, %(experiment)s)''',
                      { 'scientist': scientist, 'experiment': experiment })

    # Utility methods for conversion

    @classmethod
    def _to_association(cls, row):
        '''parses a row: user's id / name / username / email / role + experiment's id / name'''
        return {
            'user': Storage._to_user(row[0:5]).serialize(),
            'experiment': Storage._to_experiment(row[5:7]).serialize()
        }

    @classmethod
    def _to_measure(cls, row):
        '''parses a row: measure type / timestamp / experiment name / value'''
        return Measure(measure_type = row[0],
                       timestamp = row[1],
                       experiment = row[2],
                       value = row[3])

    @classmethod
    def _to_experiment(cls, row):
        '''parses a row: id / name'''
        return Experiment(experiment_id = row[0],
                          name = row[1])

    @classmethod
    def _to_user(cls, row):
        '''parses a row: id / name / username / email / role'''
        return User(user_id = row[0],
                    name = row[1],
                    username = row[2],
                    email = row[3],
                    role = row[4])

    # Utility to execute queries

    def _execute(self, statement, params, for_update = True):
        '''calls the database'''
        cur = self.cnx.cursor()
        try:
            cur.execute(statement, params)
        except mysql.connector.IntegrityError as exception:
            #TODO proper logging
            raise DbIntegrityError from exception
        if for_update:
            self.cnx.commit()
        return cur
