import unittest
from ..number_theory.gcd import gcd, gcd_recursive

class TestNumberTheoryAlgorithms(unittest.TestCase):
    
    def test_gcd(self):
        # basic cases
        self.assertEqual(gcd(0, 0), 0)        
        self.assertEqual(gcd(1, 0), 1)
        self.assertEqual(gcd(0, 1), 1)        
        self.assertEqual(gcd(1, 1), 1)
        
        # examples from wikipedia
        self.assertEqual(gcd(252, 105), 21)
        self.assertEqual(gcd(105, 252), 21)
        self.assertEqual(gcd(147, 105), 21)
        self.assertEqual(gcd(105, 147), 21)
