'''REST APIs'''

from flask import Flask,jsonify

from .storage import Storage

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

    def __init__(self, configuration:RestConfiguration, storage:Storage) -> None:
        self._configuration = configuration
        self._storage = storage

    def run(self):
        '''Main method that runs the listener'''

        app = Flask('safe repository')

        @app.route("/measures/<int:experiment_id>", methods=['GET'])
        def get_measures(experiment_id:int):
            #TODO
            user_id = 'S001'
            #TODO
            page = 1
            measures = self._storage.read_measure(experiment_id = experiment_id,
                                                  page = page,
                                                  user_id = user_id)
            return jsonify([m.serialize() for m in measures])

        app.run(host = self._configuration.host)
