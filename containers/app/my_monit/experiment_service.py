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

    def retrieve_experiments(self, current_user:str):
        '''returns all experiments'''
        return [e.serialize() for e in self._storage.read_experiments(current_user = current_user)]

    def insert_experiment(self, experiment_dict, current_user:str) -> int:
        '''inserts an experiment'''
        if self._user_service.is_admin(current_user):
            experiment = Experiment(experiment_id = None, name = experiment_dict['name'])
            return self._storage.insert_experiment(experiment)
        raise AuthorizationException