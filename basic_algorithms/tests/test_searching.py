import unittest
from ..searching.binary_search import binary_search
from ..searching.quickselect import quickselect
from ..searching.kadane import kadanes_max_subarray


class TestSearchingAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.empty_list = []
        self.sorted_list = list(range(10))
        self.custom_list = [3, 3, 0, 0, 1, 1, 2, 2]

        self.array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.positive_array = [1, 2, 3]
        self.negative_array = [-2, -1, -2, -4, -3]
    
    def test_binary_search(self):
        self.assertEqual(binary_search(self.empty_list, 0), None)
        
        self.assertEqual(binary_search(self.sorted_list, 0), 0)
        self.assertEqual(binary_search(self.sorted_list, 5), 5)
        self.assertEqual(binary_search(self.sorted_list, 9), 9)
    
    def test_quickselect(self):
        self.assertEqual(quickselect(self.sorted_list, 0), 0)
        self.assertEqual(quickselect(self.sorted_list, 5), 5)
        self.assertEqual(quickselect(self.sorted_list, 9), 9)
        
        self.assertEqual(quickselect(self.custom_list, 1), 0)
        self.assertEqual(quickselect(self.custom_list, 5), 2)

    def test_kadanes_max_subarray(self):
        self.assertEqual(kadanes_max_subarray(self.empty_list), self.empty_list)
        self.assertEqual(kadanes_max_subarray(self.array), [4, -1, 2, 1])
        self.assertEqual(kadanes_max_subarray(self.positive_array), self.positive_array)
        self.assertEqual(kadanes_max_subarray(self.negative_array), [])
        