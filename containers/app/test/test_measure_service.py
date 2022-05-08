'''unit tests'''

import unittest
from unittest.mock import Mock, MagicMock

from my_monit.measure_service import MeasuresService
from my_monit.model import Measure

class TestMeasureService(unittest.TestCase):

    def test_retrieve_measures(self):
        storage = Mock()
        measure_service = MeasuresService(storage = storage, logging = Mock())
        measures = [Measure('x','x','x',1),Measure('x','x','x',2)]
        storage.read_measure = MagicMock(return_value = measures)

        result = measure_service.retrieve_measures(1, 'x')

        self.assertEqual(len(measures), len(result))

if __name__ == '__main__':
    unittest.main()
