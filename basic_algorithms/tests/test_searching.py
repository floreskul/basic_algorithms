import unittest
from ..searching.binary_search import binary_search
from ..searching.quickselect import quickselect


class TestSearchingAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.empty_list = []
        self.sorted_list = list(range(10))
        self.custom_list = [3, 3, 0, 0, 1, 1, 2, 2]
    
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
        