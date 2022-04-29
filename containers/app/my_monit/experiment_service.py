'''Experiments business logic'''

from unicodedata import name
from .user_service import UserService
from .errors import AuthorizationException, InvalidArgument
from .storage import Storage
from .model import Experiment

class ExperimentService():
    '''Main service handling experiments'''

    def __init__(self, storage:Storage, user_service:UserService) -> None:
        self._storage = storage
        self._user_service = user_service

    # Users

    def retrieve_experiments(self, current_user:str):
        '''returns all experiments'''
        return [e.serialize() for e in self._storage.read_experiments(current_user = current_user)]

    def insert_experiment(self, experiment_dict, current_user:str) -> int:
        '''inserts an experiment'''
        if not self._user_service.is_admin(current_user):
            raise AuthorizationException
        experiment = Experiment(experiment_id = None, name = experiment_dict['name'])
        return self._storage.insert_experiment(experiment)

    def update_experiment(self, experiment_to_update:int, experiment_dict, current_user:str) -> int:
        '''updates an experiment'''
        if not self._user_service.is_admin(current_user):
            raise AuthorizationException
        current_experiment = self._storage.read_experiment(experiment_id = experiment_to_update)
        if current_experiment is None:
            # Experiment does not exist
            raise InvalidArgument

        updated_experiment = Experiment(#the experiment can't change id
                                        experiment_id = current_experiment.experiment_id,
                                        name = experiment_dict['name'])
        return self._storage.update_experiment(updated_experiment)

    # Associations

    def get_associations(self, current_user:str):
        '''returns all associations'''
        if not self._user_service.is_admin(current_user):
            raise AuthorizationException
        return self._storage.read_associations()

    def associate(self, scientist:str, experiment:int, current_user:str):
        '''associates a scientist to an experiment'''
        if not self._user_service.is_admin(current_user):
            raise AuthorizationException
        user = self._user_service.retrieve_user(user_id = scientist, current_user = current_user)
        # TODO make an enum
        if user.role != 'SCIENTIST':
            raise InvalidArgument
        self._storage.associate_scientist_experiment(scientist = scientist, experiment = experiment)