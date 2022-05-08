'''unit tests'''

import unittest
from my_monit.model import User, Experiment
from unittest.mock import Mock, MagicMock
from my_monit.rest_listener import MeasuresResource
from my_monit.rest_listener import ExperimentResource
from my_monit.rest_listener import UserResouce
from my_monit.rest_listener import ExceptionResource
from my_monit.rest_listener import ExperimentAssociationResource


from my_monit.model import Measure

def mock_flask_utilities(service):
    service.get_user = MagicMock(return_value = 'usr')
    service.to_json = MagicMock(return_value = 'json')
    service.get_request_json = MagicMock(return_value = 'json')

class TestMeasuresResource(unittest.TestCase):
    '''tests for the rest service'''

    def setUp(self):
        self.measures_service = Mock()
        self.user_service = Mock()
        self.log = Mock()
        self.measures = MeasuresResource(measures_service = self.measures_service,
                                         user_service = self.user_service,
                                         logging = self.log)
        mock_flask_utilities(self.measures)

    def test_get(self):
        _, ret = self.measures.get('exp')

        self.assertEqual(200, ret)
        self.measures_service.retrieve_measures.assert_called()
        self.log.info.assert_called()

class TestExperimentResource(unittest.TestCase):
    '''tests for the rest service'''

    def setUp(self):
        self.experiment_service = Mock()
        self.user_service = Mock()
        self.log = Mock()
        self.experiments = ExperimentResource(experiment_service = self.experiment_service,
                                              user_service = self.user_service,
                                              logging = self.log)
        mock_flask_utilities(self.experiments)

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
        mock_flask_utilities(self.users)

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
        self.user_service = Mock()
        self.exception = ExceptionResource(user_service = self.user_service, logging = self.log)

    def test_handle_error(self):
        _, ret = self.exception.handle_error('err', 'msg', 400)
        
        self.log.warn.assert_called()
        self.assertEqual(400, ret)

class TestExperimentAssociationResource(unittest.TestCase):
    '''tests for the experiment-user association'''

    def setUp(self):
        self.log = Mock()
        self.user_service = Mock()
        self.experiment_service = Mock()
        self.associations_srv = ExperimentAssociationResource(experiment_service = self.experiment_service,
                                                              user_service = self.user_service,
                                                              logging = self.log)
        mock_flask_utilities(self.associations_srv)

    def test_get(self):
        self.experiment_service.get_associations = MagicMock(return_value = [])

        _, ret = self.associations_srv.get()
        
        self.experiment_service.get_associations.assert_called()
        self.log.info.assert_called()
        self.assertEqual(200, ret)

    def test_index_by_association(self):
        associations = [
            {
                'user': User(user_id = 'user1', name = 'x', username = 'x', email = 'x', role = 'x').serialize(),
                'experiment': Experiment(experiment_id = 'experiment1', name = 'y').serialize()
            },{
                'user': User(user_id = 'user2', name = 'x', username = 'x', email = 'x', role = 'x').serialize(),
                'experiment': Experiment(experiment_id = 'experiment1', name = 'y').serialize()
            },{
                'user': User(user_id = 'user1', name = 'x', username = 'x', email = 'x', role = 'x').serialize(),
                'experiment': Experiment(experiment_id = 'experiment2', name = 'y').serialize()
            }
        ]

        result = self.associations_srv._index_by_association(associations)

        expected = {
            'experiment1': {
                'users': [{
                    'user_id': 'user1',
                    'name': 'x',
                    'email': 'x',
                    'username': 'x',
                    'role': 'x'
                },{
                    'user_id': 'user2',
                    'name': 'x',
                    'email': 'x',
                    'username': 'x',
                    'role': 'x'
                }]
            },
            'experiment2':{
                'users': [{
                    'user_id': 'user1',
                    'name': 'x',
                    'email': 'x',
                    'username': 'x',
                    'role': 'x'
                }]
            }
        }

        self.assertEquals(expected, result)

    def test_post(self):
        _, ret = self.associations_srv.post('S1', 'Exp1')
        
        self.experiment_service.associate.assert_called()
        self.log.info.assert_called()
        self.assertEqual(200, ret)

if __name__ == '__main__':
    unittest.main()
