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
        is_admin = self._storage.user_is_admin(user_id)
        self._logging.info(msg = 'is {user} admin? {is_admin}',
                           metadata = self._metadata(method = 'is_admin', user = None),
                           params={ 'user': user_id, 'is_admin': is_admin })
        return is_admin

    def read_users_by_username(self, username:str) -> User:
        '''returns User based on his uid on Firebase'''
        user = self._storage.read_users_by_username(username)
        self._logging.info(msg = 'get_user_by_uuid: found {user}',
                           metadata = self._metadata(method = 'is_admin', user = None),
                           params={ 'user': user.user_id if user is not None else '<not-found>' })
        return user

    def retrieve_users(self, current_user):
        '''returns all users'''
        if not self.is_admin(current_user):
            raise AuthorizationException
        users = self._storage.read_users()
        self._logging.info(msg = 'retrieved users: {users}',
                           metadata = self._metadata(method = 'retrieve_users',user = current_user),
                           params={ 'users': users})
        return [u.serialize() for u in users]

    def retrieve_user(self, user_id, current_user) -> User:
        '''return user with id'''
        user = self._storage.read_user(user_id = user_id, current_user = current_user)
        self._logging.info(msg = 'retrieved user: {user_id}',
                           metadata = self._metadata(method = 'retrieve_user', user = current_user),
                           params={ 'user_id': user_id })
        return user

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
            self._logging.info(msg = 'insert user: {user}',
                           metadata = self._metadata(method = 'insert_user', user = current_user),
                           params={ 'user': user })
            self._storage.insert_user(user)

    def update_user(self, user_to_update:str, user_dict, current_user:str):
        '''inserts a user'''
        if not (self.is_admin(current_user) or current_user == user_to_update):
            raise AuthorizationException
        current_version = self._storage.read_user(user_id = user_to_update,
                                               current_user = current_user)
        if current_version is None:
            # User does not exist
            raise InvalidArgument
        updated_user = User(#the user can't change id
                            user_id = current_version.user_id,
                            name = user_dict['name'],
                            email = user_dict['email'],
                            username = user_dict['username'],
                            # the user can't change role
                            role = current_version.role)
        if not updated_user.is_valid():
            # the user must be valid
            raise InvalidArgument
        if updated_user.username != current_version.username and \
            len(self._storage.read_users_by_username(updated_user.username))>0:
            # there can be no more than one user with that username
            raise InvalidArgument
        if updated_user.email != current_version.email and \
            len(self._storage.read_users_by_email(updated_user.email))>0:
            # there can be no more than one user with that email
            raise InvalidArgument
        self._logging.info(msg = 'update user: {user}',
                           metadata = self._metadata(method = 'update_user', user = current_user),
                           params={ 'user': updated_user })
        self._storage.update_user(updated_user)

    def _metadata(self, method:str, user:str):
        '''generates standardized metadata'''
        return {
            'service': 'UserService',
            'method': method,
            'user': user
        }