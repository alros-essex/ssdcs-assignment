'''REST APIs'''

from debugpy import configure
from flask import Flask

class RestConfiguration():
    '''configuration for the REST server'''

    def __init__(self, rest_host:str) -> None:
        self._rest_host = rest_host

    @property
    def host(self):
        '''returns hostname'''
        return self._rest_host

class RestListener():
    '''Creates an HTTP listener'''

    def __init__(self, configuration:RestConfiguration) -> None:
        self._configuration = configuration

    def run(self):
        '''Main method that runs the listener'''

        app = Flask('safe repository')

        @app.route("/")
        def hello():
            return "hello world!"
        app.run(host = self._configuration.host)
