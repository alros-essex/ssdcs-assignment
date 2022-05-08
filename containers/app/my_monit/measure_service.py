'''Measures business logic'''

from .storage import Storage
from .logging import Logging

class MeasuresService():
    '''Main service handling measures'''

    def __init__(self, storage:Storage, logging:Logging) -> None:
        self._storage = storage
        self._logging = logging

    def retrieve_measures(self, experiment_id:int, current_user:str):
        '''Returns an array of measures'''
        measures = self._storage.read_measure(experiment_id = experiment_id,
                                              current_user = current_user)
        self._logging.info(msg = 'retrieved {len} measures',
                           metadata = self._metadata(method = 'retrieve_measures',
                                                     user = current_user),
                           params={ 'len': len(measures) })
        return [m.serialize() for m in measures]

    def _metadata(self, method:str, user:str):
        '''generates standardized metadata'''
        return {
            'service': 'MeasuresService',
            'method': method,
            'user': user
        }
