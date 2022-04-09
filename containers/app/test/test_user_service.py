'''unit tests'''

import unittest
from unittest.mock import Mock, MagicMock

from my_monit.user_service import UserService

class TestUserService(unittest.TestCase):
    '''tests for user service'''

    def setUp(self):
        '''preparing test'''
        # mock the storage
        self.storage = Mock()

    def test_is_admin(self):
        '''test correct mapping with db'''
        self.storage.is_admin = MagicMock(return_value = True)

        user_service = UserService(storage = self.storage)

        self.assertTrue(user_service.is_admin('123'))

if __name__ == '__main__':
    unittest.main()
