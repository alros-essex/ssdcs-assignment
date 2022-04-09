'''User management services'''

from .storage import Storage

class UserService():
    '''Main service managing users'''

    def __init__(self, storage:Storage) -> None:
        '''creates the instance'''
        self._storage = storage

    def is_admin(self, user_id:str, ) -> bool:
        '''returns True if user has role ADMIN'''
        return self._storage.user_is_admin(user_id)
