import pika
import time

from storage import Storage
from rabbit_configuration import RabbitConfiguration

class RabbitListener():

    def __init__(self, configuration:RabbitConfiguration, storage:Storage) -> None:
        self._configuration = configuration
        self._storage = storage

    def run(self):
        connection = self.connect(self._configuration)
        channel = connection.channel()
        channel.queue_declare(queue='hello')

        def callback(ch, method, properties, body):
            self._storage.insert(body)

        channel.basic_consume(queue='hello',
                              auto_ack=True,
                              on_message_callback=callback)
        channel.start_consuming()

    def connect(self, configuration:RabbitConfiguration):
        '''
        connect to RabbitMQ

        Args:
            None
        Returns:
            connection
        '''
        while(True):
            try:
                return pika.BlockingConnection(pika.ConnectionParameters(configuration.url))
            except Exception as error:
                time.sleep(5)