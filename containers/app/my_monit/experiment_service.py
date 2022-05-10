'''Experiments business logic'''

from .user_service import UserService
from .errors import AuthorizationException, InvalidArgument
from .logging import Logging
from .storage import Storage
from .model import Experiment

class ExperimentService():
    '''Main service handling experiments'''

    def __init__(self, storage:Storage, user_service:UserService, logging: Logging) -> None:
        self._storage = storage
        self._user_service = user_service
        self._logging = logging

    # Users

    def retrieve_experiments(self, current_user:str):
        '''returns all experiments'''
        experiments = self._storage.read_experiments(current_user = current_user)
        self._logging.info(msg = 'retrieved {len} experiments',
                           metadata = self._metadata(method = 'retrieve_experiments',
                                                     user = current_user),
                           params={ 'len': len(experiments) })
        return [e.serialize() for e in experiments]

    def insert_experiment(self, experiment_dict, current_user:str) -> None:
        '''inserts an experiment'''
        if not self._user_service.is_admin(current_user):
            raise AuthorizationException
        experiment = Experiment(experiment_id = None, name = experiment_dict['name'])
        self._logging.info(msg = 'insert experiment: {experiment}',
                           metadata = self._metadata(method = 'insert_experiment',
                                                     user = current_user),
                           params={ 'experiment': experiment })
        self._storage.insert_experiment(experiment)

    def update_experiment(self, experiment_to_update:int, experiment_dict,
                          current_user:str) -> None:
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
        self._logging.info(msg = 'update experiment: {updated_experiment}',
                           metadata = self._metadata(method = 'update_experiment',
                                                     user = current_user),
                           params={ 'updated_experiment': updated_experiment })
        self._storage.update_experiment(updated_experiment)

    # Associations

    def get_associations(self, current_user:str):
        '''returns all associations'''
        if not self._user_service.is_admin(current_user):
            raise AuthorizationException
        associations = self._storage.read_associations()
        self._logging.info(msg = 'retrieved {len} associations',
                           metadata = self._metadata(method = 'get_associations',
                                                     user = current_user),
                           params={ 'len': len(associations) })
        return associations

    def associate(self, scientist:str, experiment:int, current_user:str):
        '''associates a scientist to an experiment'''
        if not self._user_service.is_admin(current_user):
            raise AuthorizationException
        user = self._user_service.retrieve_user(user_id = scientist, current_user = current_user)
        if user.role != 'SCIENTIST':
            raise InvalidArgument
        self._logging.info(msg = 'associating scientist {scientist} to experiment {experiment}',
                           metadata = self._metadata(method = 'associate', user = current_user),
                           params={ 'scientist': scientist, 'experiment': experiment })
        self._storage.associate_scientist_experiment(scientist = scientist, experiment = experiment)

    def _metadata(self, method:str, user:str):
        '''generates standardized metadata'''
        return {
            'service': 'ExperimentService',
            'method': method,
            'user': user
        }
