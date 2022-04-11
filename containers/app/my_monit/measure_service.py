'''Measures business logic'''

from .storage import Storage

class MeasuresService():
    '''Main service handling measures'''

    def __init__(self, storage:Storage) -> None:
        self._storage = storage

    def retrieve_measures(self, experiment_id:int, current_user:str, page:int):
        '''Returns an array of measures'''
        measures = self._storage.read_measure(experiment_id = experiment_id,
                                              page = page,
                                              current_user = current_user)
        return [m.serialize() for m in measures]
