'''REST APIs'''

from flask import Flask, request, jsonify
import jwt

from .errors import AuthorizationException, DbIntegrityError, InvalidArgument
from .logging import Logging
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
                 user_service:UserService,
                 logging: Logging) -> None:
        self._configuration = configuration
        self._experiment_service = experiment_service
        self._measures_service = measures_service
        self._user_service = user_service
        self._logging = logging

    def run(self):
        '''Main method that runs the listener'''

        app = Flask('safe repository')

        # Login
        
        @app.route("/login/", methods=['POST'])
        def create_login_user():
            '''logging in'''
            print(request)
                                                
            return 'created', 201

        @app.route("/authenticate", methods=['POST'])
        def authenticate():
            '''returns a jwt token'''
            user = request.json['username']
            # TODO replace the secret
            token = { "token": jwt.encode({"username": user}, "secret", algorithm="HS256") }
            return jsonify(token), 200

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
            self._logging.info(f'called API', metadata = {
                'api': '/users/',
                'method': 'GET',
                'user': user_id
            })
            users = self._user_service.retrieve_users(user_id)
            return jsonify(users), 200

        @app.route("/users/", methods=['POST'])
        def create_users():
            '''creates a user'''
            user_id = get_user()
            self._user_service.insert_user(current_user = user_id,
                                                   user_dict = request.json)
            return 'created', 201

        # Utilities

        def handle(exception, msg, status):
            print(exception)
            return msg, status

        @app.errorhandler(AuthorizationException)
        def handle_authorization_error(exception):
            '''user is not authorized'''
            return handle(exception, 'forbidden', 401)

        @app.errorhandler(DbIntegrityError)
        def handle_db_integrity_error(exception):
            '''some db constrain was violated'''
            return handle(exception, 'bad request', 400)
        
        @app.errorhandler(InvalidArgument)
        def handle_invalid_argument(exception):
            '''input is invalid'''
            return handle(exception, 'bad request', 400)

        @app.errorhandler(Exception)
        def handle_internal_error(exception):
            '''default error handler'''
            return handle(exception, 'internal error', 500)

        def get_user():
            token = request.headers['Authorization'].split()[1]
            decoded = jwt.decode(token, "secret", algorithms=["HS256"])
            username = decoded['username']
            return username

        # App

        app.run(host = self._configuration.host)

      

