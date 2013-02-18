import unittest
from ..searching.binary_search import binary_search


class TestSearchingAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.empty_list = []
        self.sorted_list = list(range(10))
    
    def test_binary_search(self):
        self.assertEqual(binary_search(self.empty_list, 0), None)
        
        self.assertEqual(binary_search(self.sorted_list, 0), 0)
        self.assertEqual(binary_search(self.sorted_list, 5), 5)
        self.assertEqual(binary_search(self.sorted_list, 9), 9)
        