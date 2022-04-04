import json
import datetime
import unittest

from unittest.mock import Mock, MagicMock

from my_monit.rabbit_listener import RabbitListener, RabbitConnector, RabbitConfiguration, RabbitMessageProcessor
from my_monit.model import Measure

RABBIT_URL = 'some.url'
RABBIT_USER = 'myuser'
RABBIT_PASSWORD = 'secret'
RABBIT_QUEUE = 'myqueue'

class TestRabbitListener(unittest.TestCase):

    def setUp(self):
        '''preparing test'''

        # rabbit's channel 
        self.channel = Mock()
        
        # connection
        self.connection = Mock()
        # make it return the channel
        self.connection.channel = MagicMock(return_value = self.channel)

        # stub the connector to return the connection
        RabbitConnector.connect =  MagicMock(return_value = self.connection)

        # configuration to be used
        self.configuration = RabbitConfiguration(rabbit_url = RABBIT_URL,
                                                 rabbit_user = RABBIT_USER,
                                                 rabbit_password = RABBIT_PASSWORD,
                                                 rabbit_queue = RABBIT_QUEUE)
        
        # mock processor
        self.message_processor = Mock()

        # create listener with mocked processor
        self.rabbit_listener = RabbitListener(self.configuration, self.message_processor)

        # mock the storage
        self.storage = Mock()

    def tearDown(self):
        '''cleanup things'''
        pass

    def test_connection(self):
        '''test the connectio to rabbit'''

        self.rabbit_listener.run()

        #verify
        RabbitConnector.connect.assert_called_with(self.configuration)
        self.channel.queue_declare.assert_called_with(queue = self.configuration.queue)
        self.channel.basic_consume.assert_called_with(queue = self.configuration.queue,
                                                      auto_ack = True,
                                                      on_message_callback = self.message_processor.process)

    def test_processor(self):
        '''test the processor'''

        processor = RabbitMessageProcessor(storage = self.storage)
        data = {
            'experiment': 'exp',
            'measure': 'hertz',
            'value': 10.5,
            'timestamp': 10000
        }
        msg = json.dumps(data)

        processor.process(msg)

        self.storage.assert_called_with(Measure(type = 'hertz', 
                                                timestamp = datetime.timedelta(microseconds =10000), 
                                                experiment = 'exp', 
                                                value = 10.5))

if __name__ == '__main__':
    unittest.main()