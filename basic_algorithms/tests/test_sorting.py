import unittest
import random
from ..sorting.selection_sort import selection_sort
from ..sorting.insertion_sort import insertion_sort
from ..sorting.bubble_sort import bubble_sort
from ..sorting.merge_sort import merge_sort
from ..sorting.shellsort import shellsort

class TestSortingAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.empty_list = []
        self.sorted_list = list(range(10))
        self.reverse_ordered_list = list(range(9, -1, -1))
        self.random_ordered_list = list(range(10))
        random.shuffle(self.random_ordered_list)
        
    def run_sorting_method(self, sorting_method):
        self.assertEqual(sorting_method(list(self.empty_list)),
                         self.empty_list)
        self.assertEqual(sorting_method(list(self.sorted_list)),
                         self.sorted_list)
        self.assertEqual(sorting_method(list(self.reverse_ordered_list)),
                         self.sorted_list)
        self.assertEqual(sorting_method(list(self.random_ordered_list)),
                         self.sorted_list)
    
    def test_selection_sort(self):
        self.run_sorting_method(selection_sort)
        
    def test_insertion_sort(self):
        self.run_sorting_method(insertion_sort)
    
    def test_bubble_sort(self):
        self.run_sorting_method(bubble_sort)
        
    def test_shellsort(self):
        self.run_sorting_method(shellsort)
