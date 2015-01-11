import unittest
from ..number_theory.gcd import gcd, gcd_recursive
from ..number_theory.exp_by_squaring import exp_by_squaring
from ..number_theory.sieve_of_eratosthenes import sieve_of_eratosthenes

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
    
    def test_exp_by_squaring(self):
        self.assertEqual(exp_by_squaring(2, 0), 1)
        self.assertEqual(exp_by_squaring(2, 1), 2)
        self.assertEqual(exp_by_squaring(2, 32), 2**32)
        self.assertEqual(exp_by_squaring(2, 31), 2**31)

    def test_sieve_of_eratosthenes(self):
        primes_below_10 = [2,  3,  5,  7]
        self.assertEqual(sieve_of_eratosthenes(10), primes_below_10)
        primes_below_30 = [2,  3,  5,  7,  11,  13,  17,  19,  23,  29]
        self.assertEqual(sieve_of_eratosthenes(30), primes_below_30)
