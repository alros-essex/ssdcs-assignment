'''test injection'''

from my_monit.storage import StorageConnector
from my_monit.rest_listener import RestListener
from my_monit.rabbit_listener import RabbitConnector
from my_monit.app import init
from my_monit.logging import Logging
import unittest
from unittest.mock import Mock, MagicMock

class TestContainer(unittest.TestCase):

    def test_injection(self):
        '''test dependency injection'''
        # mock stuff that connects to external services
        StorageConnector.connect = MagicMock(return_value = None)
        RestListener.run = MagicMock()
        RabbitConnector.connect = MagicMock()

        # launch init. No exceptions = all good!
        init()

if __name__ == '__main__':
    unittest.main()
