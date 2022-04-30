'''Logging / Auditing'''

from enum import Enum
import logging
import logstash
import sys

class LoggingLevel(Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

class Logging():
    '''Logging business logic'''

    def __init__(self, host:str, port:int) -> None:
        logger = logging.getLogger('python-logstash-logger')
        logger.setLevel(logging.INFO)
        #logger.addHandler(logstash.LogstashHandler(host, port, version=1))
        logger.addHandler(logstash.TCPLogstashHandler(host, port, version=1))
        self._logger = logger

    def debug(self, msg:str, metadata) -> None:
        '''information useful to debug the application'''
        self.log(msg, metadata, LoggingLevel.DEBUG)

    def info(self, msg:str, metadata) -> None:
        '''information about the application's flow'''
        self.log(msg, metadata, LoggingLevel.INFO)

    def warn(self, msg:str, metadata) -> None:
        '''abnomal behaviour that does not cause failure'''
        self.log(msg, metadata, LoggingLevel.WARN)

    def error(self, msg:str, metadata) -> None:
        '''errors are unrecoverable and cause the failure of the operation'''
        self.log(msg, metadata, LoggingLevel.ERROR)

    def critical(self, msg:str, metadata) -> None:
        '''critical errors are unrecoverable and cause the failure of the application'''
        self.log(msg, metadata, LoggingLevel.CRITICAL)

    def log(self, msg:str, metadata, level:LoggingLevel) -> None:
        '''logs an event'''
        extra = {
            'python version': repr(sys.version_info),
            'level': str(level),
            'metadata': metadata
        }
        self._logger.info(msg = msg, extra = extra)

