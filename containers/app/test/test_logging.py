'''test logging'''

from my_monit.logging import Logging
import unittest
from unittest.mock import Mock

class TestLogging(unittest.TestCase):

    def test_logging_levels(self):
        '''test logging'''
        logging = Logging('',1)
        logging._logger = Mock()
        
        logging.debug('test',{})
        expected = {
            'level': 'DEBUG',
            'metadata': {}
        }
        logging._logger.debug.assert_called_with(msg = 'test', extra = expected)

        logging.info('test',{})
        expected = {
            'level': 'INFO',
            'metadata': {}
        }
        logging._logger.info.assert_called_with(msg = 'test', extra = expected)

        logging.warn('test',{})
        expected = {
            'level': 'WARN',
            'metadata': {}
        }
        logging._logger.warning.assert_called_with(msg = 'test', extra = expected)

        logging.error('test',{})
        expected = {
            'level': 'ERROR',
            'metadata': {}
        }
        logging._logger.error.assert_called_with(msg = 'test', extra = expected)

        logging.critical('test',{})
        expected = {
            'level': 'CRITICAL',
            'metadata': {}
        }
        logging._logger.critical.assert_called_with(msg = 'test', extra = expected)

if __name__ == '__main__':
    unittest.main()
