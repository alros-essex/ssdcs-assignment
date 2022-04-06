'''Module to manage the database'''

import mysql.connector

from .model import Measure

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
            measures.append(self._to_measures(row))
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

    def _to_measures(self, row):
        '''parses a row: measure type / timestamp / experiment name / value'''
        return Measure(measure_type = row[0],
                       timestamp = row[1],
                       experiment = row[2],
                       value = row[3])

    def _execute(self, statement, params, for_update = True):
        """calls the database

        Args:
            statement: command to execute
            params: parameters for the command as a dict
        Returns:
            None
        """
        cur = self.cnx.cursor()
        cur.execute(statement, params)
        if(for_update):
            self.cnx.commit()
        return cur
