import unittest
import random
from ..sorting.selection_sort import selection_sort
from ..sorting.insertion_sort import insertion_sort

class TestSortingAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.empty_list = []
        self.sorted_list = list(range(10))
        self.reverse_ordered_list = list(range(9, -1, -1))
        self.random_ordered_list = list(range(10))
        random.shuffle(self.random_ordered_list)
    
    def test_selection_sort(self):
        self.assertEqual(selection_sort(list(self.empty_list)),
                         self.empty_list)
        self.assertEqual(selection_sort(list(self.sorted_list)),
                         self.sorted_list)
        self.assertEqual(selection_sort(list(self.reverse_ordered_list)),
                         self.sorted_list)
        self.assertEqual(selection_sort(list(self.random_ordered_list)),
                         self.sorted_list)
        
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(list(self.empty_list)),
                         self.empty_list)
        self.assertEqual(insertion_sort(list(self.sorted_list)),
                         self.sorted_list)
        self.assertEqual(insertion_sort(list(self.reverse_ordered_list)),
                         self.sorted_list)
        self.assertEqual(insertion_sort(list(self.random_ordered_list)),
                         self.sorted_list)