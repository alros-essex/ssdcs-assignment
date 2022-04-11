'''REST APIs'''

from flask import Flask, request, jsonify

from .errors import AuthorizationException, DbIntegrityError
from .measure_service import MeasuresService
from .experiment_service import ExperimentService
from .user_service import UserService

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
                 measures_service:MeasuresService,
                 user_service:UserService) -> None:
        self._configuration = configuration
        self._experiment_service = experiment_service
        self._measures_service = measures_service
        self._user_service = user_service

    def run(self):
        '''Main method that runs the listener'''

        app = Flask('safe repository')

        # Measures

        @app.route("/measures/<int:experiment_id>", methods=['GET'])
        def get_measures(experiment_id:int):
            '''retrieve measures for an experiment'''
            user_id = get_user()
            #TODO
            page = 1
            measures = self._measures_service.retrieve_measures(experiment_id = experiment_id,
                                                       current_user = user_id,
                                                       page = page)
            return jsonify(measures), 200

        # Experiments

        @app.route("/experiments/", methods=['GET'])
        def get_experiments():
            '''retrieves all experiments'''
            user_id = get_user()
            experiments = self._experiment_service.retrieve_experiments(current_user = user_id)
            return jsonify(experiments), 200

        @app.route("/experiments/", methods=['POST'])
        def post_experiment():
            '''create a new experiment'''
            user_id = get_user()
            self._experiment_service.insert_experiment(experiment_dict = request.json,
                                                       current_user = user_id)
            return 'created', 201

        # Users

        @app.route("/users/", methods=['GET'])
        def get_users():
            '''retrieves all users'''
            user_id = get_user()
            users = self._user_service.retrieve_users(user_id)
            return jsonify(users), 200

        # Utilities

        @app.errorhandler(AuthorizationException)
        def handle_authorization_error(exception):
            '''user is not authorized'''
            print(exception)
            return 'forbidden', 401

        @app.errorhandler(DbIntegrityError)
        def handle_db_integrity_error(exception):
            '''some db constrain was violated'''
            print(exception)
            return 'bad request', 400

        @app.errorhandler(Exception)
        def handle_internal_error(exception):
            '''default error handler'''
            print(exception)
            return 'internal error', 500

        def get_user():
            #TODO
            return 'A001'

        # App

        app.run(host = self._configuration.host)
