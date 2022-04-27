'''unit tests'''

import json
import unittest

from unittest.mock import Mock, MagicMock

from my_monit.rabbit_listener import RabbitListener,\
                                     RabbitConnector,\
                                     RabbitConfiguration,\
                                     RabbitMessageProcessor
from my_monit.model import Measure

RABBIT_URL = 'some.url'
RABBIT_USER = 'myuser'
RABBIT_PASSWORD = 'secret'
RABBIT_EXCHANGE = 'monit'
RABBIT_QUEUE = 'myqueue'
RABBIT_ROUTING = 'routing'

class TestRabbitListener(unittest.TestCase):
    '''tester for rabbit listener'''

    def setUp(self):
        '''preparing test'''

        # rabbit's channel
        self.channel = Mock()

        # logging
        self.logging = Mock()

        # connection
        self.connection = Mock()
        # make it return the channel
        self.connection.channel = MagicMock(return_value = self.channel)

        # stub the connector to return the connection
        self.mocked_method_connect = MagicMock(return_value = self.connection)
        RabbitConnector.connect = self.mocked_method_connect

        # configuration to be used
        self.configuration = RabbitConfiguration(rabbit_url = RABBIT_URL,
                                                 rabbit_user = RABBIT_USER,
                                                 rabbit_password = RABBIT_PASSWORD,
                                                 rabbit_exchange = RABBIT_EXCHANGE,
                                                 rabbit_routing = RABBIT_ROUTING,
                                                 rabbit_queue = RABBIT_QUEUE)

        # mock processor
        self.message_processor = Mock()

        # create listener with mocked processor
        self.rabbit_listener = RabbitListener(self.configuration,
                                              self.message_processor,
                                              logging = self.logging)

        # mock the storage
        self.storage = Mock()

    def tearDown(self):
        '''cleanup things'''

    def test_connection(self):
        '''test the connectio to rabbit'''

        self.rabbit_listener.run()

        #verify
        self.mocked_method_connect.assert_called_with(self.configuration)

        self.channel.exchange_declare.\
            assert_called_with(exchange = self.configuration.exchange,
            durable=True,
            auto_delete=False)
        self.channel.queue_declare.\
            assert_called_with(queue = self.configuration.queue,
                               durable=True,
                               exclusive=False,
                               auto_delete=False)
        self.channel.queue_bind.\
            assert_called_with(queue = self.configuration.queue,
                               exchange = self.configuration.exchange,
                               routing_key = self.configuration.routing)
        self.channel.basic_consume.\
            assert_called_with(queue = self.configuration.queue,
                               auto_ack = True,
                               on_message_callback=self.message_processor.process)

    def test_processor(self):
        '''test the processor'''

        processor = RabbitMessageProcessor(storage = self.storage, logging = self.logging)
        data = {
            'experiment': 'exp',
            'measure': 'hertz',
            'value': 10.5,
            'timestamp': 10000
        }
        msg = json.dumps(data)

        processor.process(None, None, None, msg)

        self.storage.insert_measure.\
            assert_called_with(Measure(measure_type = 'hertz',
                               timestamp = 10000,
                               experiment = 'exp',
                               value = 10.5))

if __name__ == '__main__':
    unittest.main()
