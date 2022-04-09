'''Module to manage the database'''

import mysql.connector

from .model import Measure, Experiment, User

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
    
    def read_measure(self, experiment_id:int, page:int, user_id:str):
        '''returns measures'''
        #TODO add pagination
        cur = self._execute('''SELECT ex.NAME as EXP_NAME, me.TIMESTAMP, me.MEASURE_VALUE, mt.NAME as MSR_TYPE
                            FROM MEASURES me, EXPERIMENTS ex, MEASURE_TYPES mt, USER_EXPERIMENTS ue
                            WHERE  me.EXPERIMENT_ID = ex.ID
                            AND mt.ID = me.TYPE
                            AND ue.USER_ID = %(user_id)s
                            AND ue.EXPERIMENT_ID = ex.ID
                            AND ex.ID = %(experiment_id)s
                            ORDER BY TIMESTAMP DESC''',
                            {
                                'experiment_id': experiment_id,
                                'user_id': user_id
                            },
                            for_update = False)
        measures = []
        for row in cur:
            measures.append(self._to_measure(row))
        return measures

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

    def read_experiments(self, user_id:int) -> Experiment:
        '''Retrieves all experiments visible to the user'''
        cur = self._execute('''SELECT ex.ID, ex.NAME 
                            FROM EXPERIMENTS ex, USER_EXPERIMENTS ue, USERS us, ROLES ro
                            WHERE us.ROLE = ro.ID
                            AND us.ID=%(user_id)s
                            AND ((us.ID = ue.USER_ID AND ex.ID = ue.EXPERIMENT_ID)
                            OR (ro.NAME = 'ADMIN'))''',
                            { 'user_id': user_id },
                            for_update = False)
        return [self._to_experiment(ex) for ex in cur]
        #experiments = []
        #for row in cur:
        #    experiments.append(self._to_experiment(row))
        #return experiments

    def insert_experiment(self, experiment:Experiment) -> None:
        '''inserts an experiment'''
        self._execute('''INSERT INTO EXPERIMENTS(NAME) VALUES (%(name)s)''', 
                      { 'name': experiment.name })

    def read_user(self, user_id:str, requesting_user_id:str) -> User:
        '''retrieves a user'''
        cur = self._execute('''SELECT us.ID, us.NAME, us.EMAIL, ro.NAME AS ROLE
                            FROM USERS us, ROLES ro
                            WHERE us.ROLE = ro.ID
                            AND us.ID = %(user_id)s
                            AND (%(user_id)s = %(requesting_user_id)s OR 
                            (SELECT ro.NAME 
                            FROM USERS us, ROLES ro 
                            WHERE us.ROLE = ro.ID
                            AND us.ID = %(requesting_user_id)s) = 'ADMIN')''',
                            { 'user_id': user_id, 'requesting_user_id': requesting_user_id},
                            for_update = False)
        return self._to_user(cur)

    def user_is_admin(self, user_id:str) -> bool:
        '''true if the user is admin'''
        cur = self._execute('''SELECT ro.NAME = 'ADMIN'
                            FROM USERS us, ROLES ro 
                            WHERE us.ROLE = ro.ID
                            AND us.ID = %(user_id)s''',
                            { 'user_id': user_id },
                            for_update = False)
        return [r[0] for r in cur][0] == 1

    def _to_measure(self, row):
        '''parses a row: measure type / timestamp / experiment name / value'''
        return Measure(measure_type = row[0],
                       timestamp = row[1],
                       experiment = row[2],
                       value = row[3])

    def _to_experiment(self, row):
        '''parses a row: id / name'''
        return Experiment(id = row[0],
                          name = row[1])

    def _to_user(self, row):
        '''parses a row: id / name / email / role'''
        return User(id = row[0], name = row[1], email = row[2], role = row[3])

    def _execute(self, statement, params, for_update = True):
        '''calls the database'''
        cur = self.cnx.cursor()
        cur.execute(statement, params)
        if(for_update):
            self.cnx.commit()
        return cur
