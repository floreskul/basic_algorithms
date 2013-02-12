"""
    Greatest common divisor Euclidean algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Euclidean_algorithm
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)