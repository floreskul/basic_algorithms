"""
    Exponentiation by squaring algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Exponentiation_by_squaring
"""

def exp_by_squaring(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    
    if n % 2 == 0:
        return exp_by_squaring(x * x, n // 2)
    else:
        return x * exp_by_squaring(x * x, (n - 1) // 2)