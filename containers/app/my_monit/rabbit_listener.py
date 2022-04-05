'''RabbitMQ Listener'''

import json
import datetime
import time
import pika

from .storage import Storage
from .model import Measure

class RabbitConfiguration():
    '''contains all parameters to connect to RabbitMQ'''

    def __init__(self, 
                 rabbit_url:str,
                 rabbit_user:str, 
                 rabbit_password:str, 
                 rabbit_exchange:str, 
                 rabbit_routing:str, 
                 rabbit_queue:str) -> None:
        self._rabbit_url = rabbit_url
        self._rabbit_user = rabbit_user
        self._rabbit_password = rabbit_password
        self._rabbit_exchange = rabbit_exchange
        self._rabbit_routing = rabbit_routing
        self._rabbit_queue = rabbit_queue

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

    @property
    def queue(self):
        '''return queue name'''
        return self._rabbit_queue

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, RabbitConfiguration):
            return self._rabbit_url == __o._rabbit_url \
                   and self._rabbit_user == __o._rabbit_user \
                   and self._rabbit_password == __o._rabbit_password \
                   and self._rabbit_queue == __o._rabbit_queue
        return False
    
    def __ne__(self, __o: object) -> bool:
        return not self == __o

class RabbitConnector():
    '''Utility class to simplify testing'''

    @classmethod
    def connect(cls, configuration:RabbitConfiguration) -> pika.BlockingConnection:
        '''connect to RabbitMQ'''
        while True:
            try:
                return pika.BlockingConnection(pika.ConnectionParameters(configuration.url))
            except Exception as _error:
                time.sleep(5)

class RabbitMessageProcessor():
    '''Utility to process a message'''

    def __init__(self, storage:Storage) -> None:
        self._storage = storage
    
    def process(self, _ch, _method, _properties, message) -> None:
        parsed_measure = json.loads(message)
        measure = Measure(experiment = parsed_measure['experiment'],
                          type = parsed_measure['measure'], 
                          timestamp = datetime.timedelta(microseconds = parsed_measure['timestamp']),
                          value = parsed_measure['value'])
        self._storage.insert_measure(measure)

class RabbitListener():
    '''Listens to RabbitMQ and processes messages'''

    def __init__(self, configuration:RabbitConfiguration, message_processor:RabbitMessageProcessor) -> None:
        self._configuration = configuration
        self._message_processor = message_processor

    def run(self):
        '''main method that runs the listener'''
        connection = RabbitConnector.connect(self._configuration)
        channel = connection.channel()

        channel.exchange_declare(exchange = self._configuration._rabbit_exchange,
                                 durable=True, 
                                 auto_delete=False)
        channel.queue_declare(queue = self._configuration.queue, 
                              durable=True, 
                              exclusive=False, 
                              auto_delete=False)

        channel.queue_bind(queue = self._configuration.queue, 
                           exchange = self._configuration._rabbit_exchange, 
                           routing_key = self._configuration._rabbit_routing)

        channel.basic_consume(queue = self._configuration.queue,
                              auto_ack = True,
                              on_message_callback=self._message_processor.process)

        channel.start_consuming()
