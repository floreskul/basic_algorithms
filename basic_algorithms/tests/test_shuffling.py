import unittest
import random
from ..shuffling.knuth_shuffle import knuth_shuffle

class TestShufflingAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.empty_list = []
        self.sorted_list = list(range(10))
        self.reverse_ordered_list = list(range(9, -1, -1))
        self.random_ordered_list = list(range(10))
        random.shuffle(self.random_ordered_list)
    
    def get_number_of_not_shuffled_elements(self, original, shuffled):
        not_shuffled_elements = 0
        for i in range(len(original)):
            if original[i] == shuffled[i]:
                not_shuffled_elements += 1
        return not_shuffled_elements
    
    def test_knuth_shuffle(self):
        shuffled = knuth_shuffle(list(self.empty_list))
        self.assertEqual(shuffled, self.empty_list)
        
        shuffled = knuth_shuffle(list(self.sorted_list))
        self.assertLess(self.get_number_of_not_shuffled_elements(self.sorted_list, shuffled), len(self.sorted_list) / 2)
        
        shuffled = knuth_shuffle(list(self.reverse_ordered_list))
        self.assertLess(self.get_number_of_not_shuffled_elements(self.reverse_ordered_list, shuffled), len(self.reverse_ordered_list) / 2)
        
        shuffled = knuth_shuffle(list(self.random_ordered_list))
        self.assertLess(self.get_number_of_not_shuffled_elements(self.random_ordered_list, shuffled), len(self.random_ordered_list) / 2)
