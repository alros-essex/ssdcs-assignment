'''Contains the shared model'''

class Measure():
    '''Models one Measure'''

    def __init__(self, type:str, timestamp:str, experiment:str, value:float) -> None:
        '''high level constructor where measure type and experiment are strings'''
        self._type = type
        self._timestamp = timestamp
        self._experiment = experiment
        self._value = value

    @property
    def type(self):
        '''measure type'''
        return self._type

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

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Measure):
            return self.type == __o.type \
                   and self.timestamp == __o.timestamp \
                   and self.experiment == __o.experiment \
                   and self.value == __o.value
        return False

