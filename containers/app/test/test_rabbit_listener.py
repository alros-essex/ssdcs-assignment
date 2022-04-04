import unittest

from unittest.mock import Mock, MagicMock

from my_monit.rabbit_listener import RabbitListener, RabbitConnector, RabbitConfiguration

RABBIT_URL = 'some.url'
RABBIT_USER = 'myuser'
RABBIT_PASSWORD = 'secret'

class TestRabbitListener(unittest.TestCase):

    def setUp(self):
        self.connection = Mock()
        RabbitConnector.connect =  MagicMock(return_value = self.connection)
        self.channel = Mock()
        self.connection.channel = MagicMock(return_value = self.channel)

        self.configuration = RabbitConfiguration(rabbit_url = RABBIT_URL,
                                                 rabbit_user = RABBIT_USER,
                                                 rabbit_password = RABBIT_PASSWORD)
        self.message_processor = Mock()
        self.rabbit_listener = RabbitListener(self.configuration, self.message_processor)

    def tearDown(self):
        pass

    def test_connection(self):
        self.rabbit_listener.run()

        self.configuration.connect.assert_called_with(self.configuration)
        self.channel.queue_declare.assert_called_with(self.configuration.queue())
        self.channel.basic_consume.assert_called_with(queue = self.configuration.queue(),
                                                      auto_ack = True)

if __name__ == '__main__':
    unittest.main()