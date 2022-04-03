'''Module to manage the database'''

import mysql.connector

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

    def insert_measure(self, measure) -> None:
        '''Inserts a measure'''

        data_measure = {
            'experiment_id': 100,
            'measure_id': 200,
            'measure_value': measure,
        }

        cursor = self.cnx.cursor()
        add_measure = ("INSERT INTO measures "
               "(EXPERIMENT_ID, MEASURE_ID, MEASURE_VALUE) "
               "VALUES (%(experiment_id)s, %(measure_id)s, %(measure_value)s)")
        cursor.execute(add_measure, data_measure)

        self.cnx.commit()
        cursor.close()

    def read_measure(self):
        '''returns a measure'''
        #TODO
        pass
