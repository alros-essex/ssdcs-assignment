'''unit tests'''

import unittest
from unittest.mock import Mock, MagicMock
from my_monit.model import Experiment
from my_monit.errors import AuthorizationException

from my_monit.experiment_service import ExperimentService

class TestExperimentService(unittest.TestCase):
    '''tests for user service'''

    def setUp(self):
        '''preparing test'''
        # mock the storage
        self.storage = Mock()
        self.user_service = Mock()
        self.experiment_service = ExperimentService(storage = self.storage,
                                                    user_service = self.user_service)

    def test_retrieve_experiments(self):
        '''verify the call to the storage'''
        self.storage.read_experiments = MagicMock(return_value =
                                                  [Experiment(experiment_id = 1, name = 'a'),
                                                  Experiment(experiment_id = 2, name = 'b')])
        experiments = self.experiment_service.retrieve_experiments('123')
        self.assertEqual(2, len(experiments))
        self.assertEqual(1, experiments[0]['experiment_id'])
        self.assertEqual('a', experiments[0]['name'])
        self.assertEqual(2, experiments[1]['experiment_id'])
        self.assertEqual('b', experiments[1]['name'])

    def test_insert_experiment_fail(self):
        '''only admin can insert'''
        self.user_service.is_admin = MagicMock(return_value = False)
        def insert():
            self.experiment_service.insert_experiment({}, '1234')
        self.assertRaises(AuthorizationException, insert)

    def test_insert_experiment_ok(self):
        '''verify insert'''
        self.user_service.is_admin = MagicMock(return_value = True)
        self.experiment_service.insert_experiment({'name': 'abc'}, '1234')
        self.storage.insert_experiment.assert_called_with(Experiment(experiment_id = None,
                                                                     name = 'abc'))

if __name__ == '__main__':
    unittest.main()
