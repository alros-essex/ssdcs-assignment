'''unit tests'''

import unittest
from unittest.mock import Mock, MagicMock

from my_monit.user_service import UserService
from my_monit.model import User
from my_monit.errors import AuthorizationException, InvalidArgument

class TestUserService(unittest.TestCase):
    '''tests for user service'''

    def setUp(self):
        '''preparing test'''
        # mock the storage
        self.storage = Mock()

    def test_is_admin(self):
        '''test correct mapping with db'''
        self.storage.is_admin = MagicMock(return_value = True)

        user_service = UserService(storage = self.storage, logging = Mock())

        self.assertTrue(user_service.is_admin('123'))

    def test_retrieve_users(self):
        '''test retrieval'''
        user_service = UserService(storage = self.storage, logging = Mock())
        self.storage.read_users = MagicMock(return_value = [User(user_id='x',
                                                                 name='x',
                                                                 username='x',
                                                                 email='x',
                                                                 role='x')])
        user_service.is_admin = MagicMock(return_value = True)
        users = user_service.retrieve_users('usr')
        self.assertEquals(1, len(users))

    def test_retrieve_users_unauthorised(self):
        '''test retrieval from unauthorised user'''
        user_service = UserService(storage = self.storage, logging = Mock())
        self.storage.read_users = MagicMock(return_value = [User(user_id='x',
                                                                 name='x',
                                                                 username='x',
                                                                 email='x',
                                                                 role='x')])
        user_service.is_admin = MagicMock(return_value = False)
        
        self.assertRaises(AuthorizationException, user_service.retrieve_users, 'usr')

    def test_insert_user(self):
        '''test insert logic'''
        user_service = UserService(storage = self.storage, logging = Mock())
        user_service.is_admin = MagicMock(return_value = True)
        self.storage.read_users_by_username = MagicMock(return_value = [])
        self.storage.read_users_by_email = MagicMock(return_value = [])

        user_service.insert_user({
            'user_id':'x',
            'name': 'x',
            'email': 'x',
            'username': 'x',
            'role': 'x'
        }, 'usr')

        self.storage.insert_user.assert_called_with(User('x','x','x','x','x'))


    def test_update_user(self):
        '''test update logic'''
        user_service = UserService(storage = self.storage, logging = Mock())
        user_service.is_admin = MagicMock(return_value = True)
        self.storage.read_user = MagicMock(return_value = User('x','x','x','x','x'))
        self.storage.read_users_by_username = MagicMock(return_value = [])
        self.storage.read_users_by_email = MagicMock(return_value = [])

        user_service.update_user('x',{
            'name':'y',
            'email':'y',
            'username':'y'
        },'x')
        
        self.storage.update_user.assert_called_with(User('x','y','y','y','x'))

    def test_read_users_by_username(self):
        '''test user retrieval logic'''
        user_service = UserService(storage = self.storage, logging = Mock())
        user = User('x','x','x','x','x')
        self.storage.read_users_by_username = MagicMock(return_value = user)

        result = user_service.read_users_by_username('x')
        
        self.assertEquals(user, result)

    def test_retrieve_users(self):
        '''test user retrieval logic'''
        user_service = UserService(storage = self.storage, logging = Mock())
        user = User('x','x','x','x','x')
        self.storage.read_user = MagicMock(return_value = user)

        result = user_service.retrieve_user('x', 'y')
        
        self.assertEquals(user, result)

if __name__ == '__main__':
    unittest.main()
