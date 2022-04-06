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

    def read_measure(self):
        '''returns a measure'''
        #TODO

    def _execute(self, statement, params):
        """calls the database

        Args:
            statement: command to execute
            params: parameters for the command as a dict
        Returns:
            None
        """
        cur = self.cnx.cursor()
        cur.execute(statement, params)
        self.cnx.commit()
        return cur
