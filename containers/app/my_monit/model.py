'''Contains the shared model'''

class Measure():
    '''Models one Measure'''

    def __init__(self, measure_type:str, timestamp:str, experiment:str, value:float) -> None:
        '''high level constructor where measure type and experiment are strings'''
        self._measure_type = measure_type
        self._timestamp = timestamp
        self._experiment = experiment
        self._value = value

    @property
    def measure_type(self):
        '''measure type'''
        return self._measure_type

    @property
    def timestamp(self):
        '''timestamp of the recording'''
        return self._timestamp

    @property
    def experiment(self):
        '''name of the experiment'''
        return self._experiment

    @property
    def value(self):
        '''value of the measure'''
        return self._value

    def serialize(self):
        '''serialize into a dict'''
        return {
            "measure_type": self.measure_type,
            "timestamp": self.timestamp,
            "experiment": self.experiment,
            "value": self.value
        }

    def __eq__(self, __o: object) -> bool:
        '''equals'''
        return isinstance(__o, Measure) and \
               self.measure_type == __o.measure_type \
               and self.timestamp == __o.timestamp \
               and self.experiment == __o.experiment \
               and self.value == __o.value

    def __ne__(self, __o: object) -> bool:
        '''not equals'''
        return not self == __o

class Experiment():
    '''Models one experiment'''

    def __init__(self, experiment_id:int, name:str) -> None:
        '''creates the instance'''
        self._experiment_id = experiment_id
        self._name = name

    @property
    def experiment_id(self):
        '''experiment id'''
        return self._experiment_id

    @property
    def name(self):
        '''experiment name'''
        return self._name

    def serialize(self):
        '''serialize into a dict'''
        return {
            "experiment_id": self._experiment_id,
            "name": self._name
        }

    def __eq__(self, __o: object) -> bool:
        '''equals'''
        return isinstance(__o, Experiment) and \
               self.experiment_id == __o.experiment_id \
               and self.name == __o.name

    def __ne__(self, __o: object) -> bool:
        '''not equals'''
        return not self.__eq__(__o)

class User():
    '''Models a user'''

    def __init__(self, user_id:str, name:str, username:str, email:str, role:str) -> None:
        '''creates the instance'''
        self._user_id = user_id
        self._name = name
        self._username = username
        self._email = email
        self._role = role

    def is_valid(self) -> bool:
        '''true is the entity is valid'''
        def is_not_blank(string):
            return string and string.strip()
        return is_not_blank(self.user_id) \
               and is_not_blank(self.name) \
               and is_not_blank(self.username) \
               and is_not_blank(self.email) \
               and is_not_blank(self.role)

    @property
    def user_id(self):
        '''user id'''
        return self._user_id

    @property
    def name(self):
        '''user's name'''
        return self._name

    @property
    def username(self):
        '''user's username'''
        return self._username

    @property
    def email(self):
        '''user's email'''
        return self._email

    @property
    def role(self):
        '''user's role'''
        return self._role

    def serialize(self):
        '''serialize into a dict'''
        return {
            "user_id": self._user_id,
            "name": self._name,
            "username": self._username,
            "email": self._email,
            "role": self._role
        }

    def __eq__(self, __o: object) -> bool:
        '''equals'''
        return isinstance(__o, User) and \
               self.user_id == __o.user_id \
               and self.name == __o.name \
               and self.username == __o.username \
               and self._email == __o.email \
               and self._role == __o._role

    def __ne__(self, __o: object) -> bool:
        '''not equals'''
        return not self.__eq__(__o)
