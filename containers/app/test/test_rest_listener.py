'''unit tests'''

import logging
import unittest
from unittest.mock import Mock, MagicMock
from my_monit.rest_listener import MeasuresResource

from my_monit.user_service import UserService
from my_monit.model import Measure

class TestMeasuresResource(unittest.TestCase):
    '''tests for the rest service'''

    def setUp(self):
        self.measures_service = Mock()
        self.log = Mock()
        self.measures = MeasuresResource(measures_service = self.measures_service,
                                         logging = self.log)
        self.measures.get_user = MagicMock(return_value = 'usr')
        self.measures.to_json = MagicMock(return_value = 'json')

    def test_measures(self):
        srz = Measure('x','x','x',1).serialize()
        self.measures_service.retrieve_measures = MagicMock(return_value = [srz])

        _, ret = self.measures.get('exp', 1)

        self.assertEqual(200, ret)
        self.log.info.assert_called()
        
if __name__ == '__main__':
    unittest.main()
