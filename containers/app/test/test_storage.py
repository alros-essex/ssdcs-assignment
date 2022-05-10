'''unit tests'''

import unittest
import mysql

from my_monit.storage import Storage
from my_monit.errors import DbIntegrityError
from unittest.mock import Mock, MagicMock

class TestStorage(unittest.TestCase):

    def test_execute(self):
        '''test the execution of all queries'''
        storage = Storage(Mock(), Mock())
        storage.cnx = Mock()
        cur = Mock()
        storage.cnx.cursor = MagicMock(return_value = cur)

        storage._execute('st', {'k':'v'}, for_update = False)

        cur.execute.assert_called_with('st',{'k':'v'})

    def test_execute_for_update(self):
        '''test the execution of all queries'''
        storage = Storage(Mock(), Mock())
        storage.cnx = Mock()
        cur = Mock()
        storage.cnx.cursor = MagicMock(return_value = cur)

        storage._execute('st', {'k':'v'})

        cur.execute.assert_called_with('st',{'k':'v'})
        storage.cnx.commit.assert_called()

    def test_execute_fail(self):
        '''test the execution of all queries'''
        storage = Storage(Mock(), Mock())
        storage.cnx = Mock()
        cur = Mock()
        cur.execute = MagicMock(side_effect=mysql.connector.IntegrityError)
        storage.cnx.cursor = MagicMock(return_value = cur)

        self.assertRaises(DbIntegrityError, storage._execute, 'st', {'k':'v'})

if __name__ == '__main__':
    unittest.main()
