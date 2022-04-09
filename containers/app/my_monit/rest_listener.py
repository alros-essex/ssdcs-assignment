'''REST APIs'''

from flask import Flask, request, jsonify
import json

from .errors import AuthorizationException
from .measure_service import MeasuresService
from .experiment_service import ExperimentService

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

    def __init__(self, 
                 configuration:RestConfiguration,
                 experiment_service:ExperimentService,
                 measures_service:MeasuresService) -> None:
        self._configuration = configuration
        self._experiment_service = experiment_service
        self._measures_service = measures_service

    def run(self):
        '''Main method that runs the listener'''

        app = Flask('safe repository')

        @app.route("/measures/<int:experiment_id>", methods=['GET'])
        def get_measures(experiment_id:int):
            '''retrieve measures for an experiment'''
            #TODO
            user_id = 'S001'
            #TODO
            page = 1
            measures = self._measures_service.retrieve_measures(experiment_id = experiment_id,
                                                       user_id = user_id,
                                                       page = page)
            return jsonify(measures), 200

        @app.route("/experiments/", methods=['GET'])
        def get_experiments():
            '''retrieves all experiments'''
            #TODO
            user_id = 'S001'
            experiments = self._experiment_service.retrieve_experiments(user_id = user_id)
            return jsonify(experiments), 200

        @app.route("/experiments/", methods=['POST'])
        def post_experiment():
            '''create a new experiment'''
            #TODO
            user_id = 'S001'
            self._experiment_service.insert_experiment(experiment_dict = request.json, user_id = user_id)
            return 'created', 201

        @app.errorhandler(AuthorizationException)
        def handle_authorization_error(e):
            '''user is not authorized'''
            return 'forbidden', 401

        @app.errorhandler(Exception)
        def handle_internal_error(e):
            '''default error handler'''
            print(e)
            return 'internal error', 500

        app.run(host = self._configuration.host)
