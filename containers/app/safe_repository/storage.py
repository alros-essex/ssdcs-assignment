import mysql.connector

class Storage():

    def __init__(self) -> None:
        self.cnx = mysql.connector.connect(user='root', password='password',
                                           host='mysql',
                                           database='safe_repository')

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