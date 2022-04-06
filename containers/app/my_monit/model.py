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

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Measure):
            return self.measure_type == __o.measure_type \
                   and self.timestamp == __o.timestamp \
                   and self.experiment == __o.experiment \
                   and self.value == __o.value
        return False

    def __ne__(self, __o: object) -> bool:
        return not self == __o
