'''unit tests'''

import logging
import unittest
from unittest.mock import Mock, MagicMock
from my_monit.rest_listener import MeasuresResource, ExperimentResource, UserResouce, ExceptionResource

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

    def test_get(self):
        _, ret = self.measures.get('exp', 1)

        self.assertEqual(200, ret)
        self.measures_service.retrieve_measures.assert_called()
        self.log.info.assert_called()

class TestExperimentResource(unittest.TestCase):
    '''tests for the rest service'''

    def setUp(self):
        self.experiment_service = Mock()
        self.log = Mock()
        self.experiments = ExperimentResource(experiment_service = self.experiment_service,
                                                  logging = self.log)
        self.experiments.get_user = MagicMock(return_value = 'usr')
        self.experiments.to_json = MagicMock(return_value = 'json')
        self.experiments.get_request_json = MagicMock(return_value = 'json')

    def test_get(self):
        _, ret = self.experiments.get()

        self.experiment_service.retrieve_experiments.assert_called()
        self.log.info.assert_called()
        self.assertEqual(200, ret)

    def test_post(self):
        _, ret = self.experiments.post()

        self.experiment_service.insert_experiment.assert_called()
        self.log.info.assert_called()
        self.assertEqual(201, ret)

    def test_put(self):
        _, ret = self.experiments.put('1')

        self.experiment_service.update_experiment.assert_called()
        self.log.info.assert_called()
        self.assertEqual(200, ret)
        
class TestUserResource(unittest.TestCase):
    '''tests for the rest service'''

    def setUp(self):
        self.user_service = Mock()
        self.log = Mock()
        self.users = UserResouce(user_service = self.user_service,
                                 logging = self.log)
        self.users.get_user = MagicMock(return_value = 'usr')
        self.users.to_json = MagicMock(return_value = 'json')
        self.users.get_request_json = MagicMock(return_value = 'json')

    def test_get(self):
        _, ret = self.users.get()
        
        self.user_service.retrieve_users.assert_called()
        self.log.info.assert_called()
        self.assertEqual(200, ret)

    def test_post(self):
        _, ret = self.users.post()

        self.user_service.insert_user.assert_called()
        self.log.info.assert_called()
        self.assertEqual(201, ret)

    def test_put(self):
        _, ret = self.users.put('usr')

        self.user_service.update_user.assert_called()
        self.log.info.assert_called()
        self.assertEqual(200, ret)

class TestExceptionResource(unittest.TestCase):
    '''tests for the rest service'''

    def setUp(self):
        self.log = Mock()
        self.exception = ExceptionResource(logging = self.log)

    def test_handle_error(self):
        _, ret = self.exception.handle_error('err', 'msg', 400)
        
        self.log.warn.assert_called()
        self.assertEqual(400, ret)


if __name__ == '__main__':
    unittest.main()
