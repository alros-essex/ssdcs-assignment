'''test the model'''

import unittest
from my_monit.model import User

class TestModel(unittest.TestCase):

    def setUp(self):
        '''preparing test'''
        pass
    
    def _user(self, user_id, name, email, username, role) -> User:
        return User(user_id = user_id,
                        name = name,
                        email = email,
                        username = username,
                        role = role)

    def test_valid_user(self):
        self.assertTrue(self._user('aa','bb','cc','dd','ee').is_valid())

    def test_invalid_users(self):
        self.assertFalse(self._user('','b','c','d','e').is_valid())
        self.assertFalse(self._user('a','','c','d','e').is_valid())
        self.assertFalse(self._user('a','b','','d','e').is_valid())
        self.assertFalse(self._user('a','b','c','','e').is_valid())
        self.assertFalse(self._user('a','b','c','d','').is_valid())
        self.assertFalse(self._user(None,'b','c','d','e').is_valid())
        self.assertFalse(self._user('a',None,'c','d','e').is_valid())
        self.assertFalse(self._user('a','b',None,'d','e').is_valid())
        self.assertFalse(self._user('a','b','c',None,'e').is_valid())
        self.assertFalse(self._user('a','b','c','d',None).is_valid())

if __name__ == '__main__':
    unittest.main()
