"""
    Sieve of Eratosthenes algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
import math


def sieve_of_eratosthenes(n):
    is_prime = [False, False] + [True] * (n - 2)
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i**2, n, i):
                is_prime[j] = False
    return [x for x in range(2, n) if is_prime[x]]