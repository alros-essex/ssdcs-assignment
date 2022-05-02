'''User management services'''

from .storage import Storage
from .errors import AuthorizationException, InvalidArgument
from .logging import Logging
from .model import User, LoggingModel

class UserService():
    '''Main service managing users'''

    def __init__(self, storage:Storage, logging: Logging) -> None:
        '''creates the instance'''
        self._storage = storage
        self._logging = logging

    def is_admin(self, user_id:str, ) -> bool:
        '''returns True if user has role ADMIN'''
        return self._storage.user_is_admin(user_id)

    def retrieve_users(self, current_user):
        '''returns all users'''
        if not self.is_admin(current_user):
            raise AuthorizationException
        users = self._storage.read_users()
        self._log(msg = 'users: {users}', method = 'retrieve_users', current_user = current_user, params={ 'users': users})
        return [u.serialize() for u in users]

    def retrieve_user(self, user_id, current_user) -> User:
        '''return user with id'''
        return self._storage.read_user(user_id = user_id, current_user = current_user)

    def insert_user(self, user_dict, current_user):
        '''inserts a user'''
        if self.is_admin(current_user):
            user = User(user_id = user_dict['user_id'],
                        name = user_dict['name'],
                        email = user_dict['email'],
                        username = user_dict['username'],
                        role = user_dict['role'])
            if not user.is_valid() or \
                len(self._storage.read_users_by_username(user.username))>0 or \
                len(self._storage.read_users_by_email(user.email))>0:
                raise InvalidArgument
            return self._storage.insert_user(user)

    def update_user(self, user_to_update:str, user_dict, current_user:str):
        '''inserts a user'''
        if not (self.is_admin(current_user) or current_user == user_to_update):
            raise AuthorizationException
        current_user = self._storage.read_user(user_id = user_to_update,
                                               current_user = current_user)
        if current_user is None:
            # User does not exist
            raise InvalidArgument
        updated_user = User(#the user can't change id
                            user_id = current_user.user_id,
                            name = user_dict['name'],
                            email = user_dict['email'],
                            username = user_dict['username'],
                            # the user can't change role
                            role = current_user.role)
        if not updated_user.is_valid():
            # the user must be valid
            raise InvalidArgument
        if updated_user.username != current_user.username and \
            len(self._storage.read_users_by_username(updated_user.username))>0:
            # there can be no more than one user with that username
            raise InvalidArgument
        if updated_user.email != current_user.email and \
            len(self._storage.read_users_by_email(updated_user.email))>0:
            # there can be no more than one user with that email
            raise InvalidArgument
        return self._storage.update_user(updated_user)

    @LoggingModel.is_logging
    def _log(self, msg:str, method:str, current_user:str, params=None):
        formatted_msg = msg.format(**params)
        self._logging.info(formatted_msg, metadata = self._metadata(method = method, user = current_user))

    def _metadata(self, method:str, user:str):
        '''generates standardized metadata'''
        return {
            'service': 'UserService',
            'method': method,
            'user': user
        }