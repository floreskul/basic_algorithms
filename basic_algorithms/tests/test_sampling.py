import unittest
from ..sampling.reservoir_sampling import reservoir_sampling


class TestSamplingAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.x = list(range(20))
    
    def test_reservoir_sampling(self):
        sample = reservoir_sampling(self.x, 5)
        s = set(sample)

    	self.assertEqual(len(sample), 5)
    	self.assertEqual(len(s), 5)
    	self.assertTrue(s.issubset(self.x))
