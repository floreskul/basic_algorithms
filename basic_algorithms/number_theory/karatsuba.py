"""
    Karatsuba fast multiplication algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Karatsuba_algorithm
"""

def karatsuba_multiplication(x, y):
	if x < 10 or y < 10:
		return x * y

	m = max(len(str(x)) / 2, len(str(y)) / 2)
	x1, x0 = divmod(x, 10**m)
	y1, y0 = divmod(y, 10**m)

	z0 = karatsuba_multiplication(x0, y0)
	z2 = karatsuba_multiplication(x1, y1)
	z1 = karatsuba_multiplication(x0 + x1, y0 + y1) - z2 - z0

	return z2 * 10**(2 * m) + 10**m * z1 + z0
