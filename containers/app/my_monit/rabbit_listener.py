'''RabbitMQ Listener'''

import time
import pika

from storage import Storage

class RabbitConfiguration():
    '''contains all parameters to connect to RabbitMQ'''

    def __init__(self, rabbit_url:str, rabbit_user:str, rabbit_password:str) -> None:
        self._rabbit_url = rabbit_url
        self._rabbit_user = rabbit_user
        self._rabbit_password = rabbit_password

    @property
    def url(self):
        '''returns url'''
        return self._rabbit_url

    @property
    def user(self):
        '''returns username'''
        return self._rabbit_user

    @property
    def password(self):
        '''returns password'''
        return self._rabbit_password

class RabbitListener():
    '''Listens to RabbitMQ and processes messages'''

    def __init__(self, configuration:RabbitConfiguration, storage:Storage) -> None:
        self._configuration = configuration
        self._storage = storage

    def run(self):
        '''main method that runs the listener'''
        connection = RabbitListener.connect(self._configuration)
        channel = connection.channel()
        channel.queue_declare(queue='hello')

        def callback(_ch, _method, _properties, body):
            self._storage.insert(body)

        channel.basic_consume(queue='hello',
                              auto_ack=True,
                              on_message_callback=callback)
        channel.start_consuming()

    @classmethod
    def connect(cls, configuration:RabbitConfiguration):
        '''connect to RabbitMQ'''
        while True:
            try:
                return pika.BlockingConnection(pika.ConnectionParameters(configuration.url))
            except Exception as _error:
                time.sleep(5)
