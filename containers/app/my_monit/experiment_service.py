'''Experiments business logic'''

from .user_service import UserService
from .errors import AuthorizationException
from .storage import Storage
from .model import Experiment

class ExperimentService():
    '''Main service handling experiments'''

    def __init__(self, storage:Storage, user_service:UserService) -> None:
        self._storage = storage
        self._user_service = user_service

    def retrieve_experiments(self, user_id:str):
        '''returns all experiments'''
        return [e.serialize() for e in self._storage.read_experiments(user_id = user_id)]

    def insert_experiment(self, experiment_dict, user_id:str) -> int:
        '''inserts an experiment and returns its id'''
        if self._user_service.is_admin(user_id):
            experiment = Experiment(experiment_id = None, name = experiment_dict['name'])
            return self._storage.insert_experiment(experiment)
        raise AuthorizationException
