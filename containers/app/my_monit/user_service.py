'''User management services'''

from .storage import Storage
from .errors import AuthorizationException

class UserService():
    '''Main service managing users'''

    def __init__(self, storage:Storage) -> None:
        '''creates the instance'''
        self._storage = storage

    def is_admin(self, user_id:str, ) -> bool:
        '''returns True if user has role ADMIN'''
        return self._storage.user_is_admin(user_id)

    def retrieve_users(self, current_user):
        '''returns all users'''
        if not self.is_admin(current_user):
            raise AuthorizationException
        return [u.serialize() for u in self._storage.read_users()]