import mysql.connector

from storage_configuration import StorageConfiguration

class Storage():

    def __init__(self, storage_configuration:StorageConfiguration) -> None:
        self.cnx = mysql.connector.connect(user = storage_configuration.user, 
                                           password = storage_configuration.password,
                                           host = storage_configuration.host,
                                           database = storage_configuration.database)

    def insert(self, measure) -> None:

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