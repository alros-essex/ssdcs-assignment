'''REST APIs'''

from abc import ABC
from flask import Flask, request, jsonify
from itsdangerous import json
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

class FlaskResource(ABC):
    '''Base class for Flask Resources'''

    def __init__(self, logging:Logging) -> None:
        '''build the instance'''
        self._logging = logging

    def log_info(self, msg:str, metadata):
        '''logs at info level'''
        self._logging.info(msg = msg, metadata = metadata)

    def get_user(self):
        '''retrieves the user from the request'''
        token = request.headers['Authorization'].split()[1]
        # TODO
        decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
        username = decoded['username']
        return username

    def metadata(self, api:str, method:str, user:str):
        '''generates standardized metadata'''
        return {
            'service': 'RestListener',
            'api': api,
            'method': method,
            'user': user
        }

    def to_json(self, obj):
        '''indirection to make testing easier'''
        return jsonify(obj)

class MeasuresResource(FlaskResource):
    '''resource mapping the measures'''

    def __init__(self, measures_service:MeasuresService, logging: Logging) -> None:
        '''builds the instance'''
        super().__init__(logging)
        self._measure_service = measures_service

    def get(self, experiment_id:int, page:int):
        '''retrieve measures for an experiment'''
        user_id = self.get_user()
        self.log_info('called API', metadata = self.metadata(api = '/measures/<int:experiment_id>',
                                                              method = 'GET',
                                                              user = user_id))
        measures = self._measure_service.retrieve_measures(experiment_id = experiment_id,
                                                            current_user = user_id,
                                                            page = page)
        return self.to_json(measures), 200

class ExperimentResource(FlaskResource):
    '''resource mapping the experiments'''

    def __init__(self, experiment_service:ExperimentService, logging: Logging) -> None:
        '''builds the instance'''
        super().__init__(logging)
        self._experiment_service = experiment_service

    def get(self):
        '''retrieves all experiments'''
        user_id = self.get_user()
        self._logging.info('called API', metadata = self.metadata(api = '/experiments/',
                                                                   method = 'GET',
                                                                   user = user_id))
        experiments = self._experiment_service.retrieve_experiments(current_user = user_id)
        return jsonify(experiments), 200

    def post(self):
        '''create a new experiment'''
        user_id = self.get_user()
        self._logging.info('called API', metadata = self.metadata(api = '/experiments/',
                                                                   method = 'POST',
                                                                   user = user_id))
        self._experiment_service.insert_experiment(experiment_dict = request.json,
                                                       current_user = user_id)
        return 'created', 201

class UserResouce(FlaskResource):
    '''resource mapping users'''

    def __init__(self, user_service:UserService, logging: Logging) -> None:
        '''builds the instance'''
        super().__init__(logging)
        self._user_service = user_service

    def get(self):
        '''retrieves all users'''
        user_id = self.get_user()
        self._logging.info('called API', metadata = self.metadata(api = '/users/',
                                                                   method = 'GET',
                                                                   user = user_id))
        users = self._user_service.retrieve_users(user_id)
        return jsonify(users), 200

    def post(self):
        '''creates a user'''
        user_id = self.get_user()
        self._logging.info('called API', metadata = self.metadata(api = '/users/',
                                                                   method = 'POST',
                                                                   user = user_id))
        self._user_service.insert_user(current_user = user_id,
                                       user_dict = request.json)
        return 'created', 201

    def put(self, user_to_update:str):
        '''updates a user'''
        user_id = self.get_user()
        self._logging.info('called API', metadata = self.metadata(api = '/users/',
                                                                   method = 'PUT',
                                                                   user = user_id))
        self._user_service.update_user(current_user = user_id,
                                       user_to_update = user_to_update,
                                       user_dict = request.json)
        return 'updated', 200

class ExceptionResource(FlaskResource):
    '''resource mapping all exceptions'''

    def __init__(self, logging: Logging) -> None:
        '''builds the instance'''

    def handle_error(self, exception, message:str, http_status:int):
        '''handles all errors logging them in a standard way'''
        log = self._logging.warn if http_status<500 else self._logging.error
        log('exception in rest call', metadata = {
            'service': 'RestListener',
            'exception': str(exception),
            'httpstatus': http_status
        })
        print(exception)
        return message, http_status

class RestListener():
    '''Creates an HTTP listener'''

    def __init__(self,
                 configuration:RestConfiguration,
                 experiment_service:ExperimentService,
                 measures_service:MeasuresService,
                 user_service:UserService,
                 logging: Logging) -> None:
        self._configuration = configuration
        self._measure_resource = MeasuresResource(measures_service = measures_service,
                                                  logging = logging)
        self._experiment_resource = ExperimentResource(experiment_service = experiment_service,
                                                       logging = logging)
        self._user_resource = UserResouce(user_service = user_service, logging = logging)
        self._exception_resource = ExceptionResource(logging = logging)

    def run(self):
        '''Main method that runs the listener'''

        app = Flask('safe repository')

        # Login

        @app.route('/login/', methods=['POST'])
        def create_login_user():
            '''logging in'''
            print(request)
            return 'created', 201

        @app.route('/authenticate', methods=['POST'])
        def authenticate():
            '''returns a jwt token'''
            user = request.json['username']
            # TODO replace the secret
            token = { 'token': jwt.encode({'username': user}, 'secret', algorithm='HS256') }
            return jsonify(token), 200

        # Measures

        @app.route('/measures/<int:experiment_id>', methods=['GET'])
        def get_measures(experiment_id:int):
            '''retrieve measures for an experiment'''
            # TODO
            page = 1
            return self._measure_resource.get(experiment_id = experiment_id)

        # Experiments

        @app.route('/experiments/', methods=['GET'])
        def get_experiments():
            '''retrieves all experiments'''
            return self._experiment_resource.get()

        @app.route('/experiments/', methods=['POST'])
        def post_experiment():
            '''create a new experiment'''
            return self._experiment_resource.post()

        # Users

        @app.route('/users/', methods=['GET'])
        def get_users():
            '''retrieves all users'''
            return self._user_resource.get()

        @app.route('/users/', methods=['POST'])
        def create_users():
            '''creates a user'''
            return self._user_resource.post()

        @app.route('/users/<user>', methods=['PUT'])
        def update_user(user):
            '''updates a user'''
            return self._user_resource.put(str(user))

        # Utilities

        def handle(exception, msg, status):
            print(exception)
            return msg, status

        @app.errorhandler(AuthorizationException)
        def handle_authorization_error(exception):
            '''user is not authorized'''
            return self._exception_resource.handle_error(exception = exception,
                                                         message = 'forbidden',
                                                         http_status = 401)

        @app.errorhandler(DbIntegrityError)
        def handle_db_integrity_error(exception):
            '''some db constrain was violated'''
            return self._exception_resource.handle_error(exception = exception,
                                                         message = 'bad request',
                                                         http_status = 400)

        @app.errorhandler(InvalidArgument)
        def handle_invalid_argument(exception):
            '''input is invalid'''
            return self._exception_resource.handle_error(exception = exception,
                                                         message = 'bad request',
                                                         http_status = 400)

        @app.errorhandler(Exception)
        def handle_internal_error(exception):
            '''default error handler'''
            return self._exception_resource.handle_error(exception = exception,
                                                         message = 'internal error',
                                                         http_status = 500)

        # App

        app.run(host = self._configuration.host)
