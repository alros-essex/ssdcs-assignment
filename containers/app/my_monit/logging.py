'''Logging / Auditing'''

from enum import Enum
import logging
import logstash
import sys
from .model import LoggingModel
from colorama import Fore

class LoggingLevel(Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

    def __str__(self) -> str:
        return self.value

class Logging():
    '''Logging business logic'''

    def __init__(self, host:str, port:int) -> None:
        logger = logging.getLogger('python-logstash-logger')
        logger.setLevel(logging.INFO)
        #logger.addHandler(logstash.LogstashHandler(host, port, version=1))
        logger.addHandler(logstash.TCPLogstashHandler(host, port, version=1))
        self._logger = logger

    def debug(self, msg:str, metadata, params=None) -> None:
        '''information useful to debug the application'''
        self.log(msg, metadata, LoggingLevel.DEBUG, params)

    def info(self, msg:str, metadata, params=None) -> None:
        '''information about the application's flow'''
        self.log(msg, metadata, LoggingLevel.INFO, params)

    def warn(self, msg:str, metadata, params=None) -> None:
        '''abnomal behaviour that does not cause failure'''
        self.log(msg, metadata, LoggingLevel.WARN, params)

    def error(self, msg:str, metadata, params=None) -> None:
        '''errors are unrecoverable and cause the failure of the operation'''
        self.log(msg, metadata, LoggingLevel.ERROR, params)

    def critical(self, msg:str, metadata, params=None) -> None:
        '''critical errors are unrecoverable and cause the failure of the application'''
        self.log(msg, metadata, LoggingLevel.CRITICAL, params)

    _logging_color = {
        LoggingLevel.CRITICAL: Fore.RED,
        LoggingLevel.ERROR: Fore.RED,
        LoggingLevel.WARN: Fore.YELLOW,
        LoggingLevel.INFO: Fore.GREEN,
        LoggingLevel.DEBUG: Fore.GREEN
    }

    @LoggingModel.is_logging
    def log(self, msg:str, metadata, level:LoggingLevel, params=None) -> None:
        '''logs an event'''
        try:
            formatted_msg = msg.format(**params) if params is not None else msg
            extra = {
                'level': str(level),
                'metadata': metadata
            }
            color = Logging._logging_color[level]
            print(f'{level} - {color}{extra}{Fore.RESET} - {formatted_msg}')

            if level is LoggingLevel.DEBUG:
                self._logger.debug(msg = formatted_msg, extra = extra)
            elif level is LoggingLevel.INFO:
                self._logger.info(msg = formatted_msg, extra = extra)
            elif level is LoggingLevel.WARN:
                self._logger.warn(msg = formatted_msg, extra = extra)
            elif level is LoggingLevel.ERROR:
                self._logger.error(msg = formatted_msg, extra = extra)
            else:
                self._logger.critical(msg = formatted_msg, extra = extra)
        except Exception as ex:
            print(f'{ex}')

