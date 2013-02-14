"""
    Shellsort algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Shellsort
"""
from math import log

def shellsort(x):
    n = len(x)
    if n <= 1:
        return x
    # use original Shell's gaps: [floor(n/2), floor(n/4), ..., 1]  
    gaps = [int(n / 2**i) for i in range(1, int(log(n, 2) + 1))]
    for gap in gaps:
        # run insertion sort for this gap
        for i in range(gap, n):
            value_to_insert = x[i]
            hole_position = i
            # shift elements right by gap until there is found the right place
            while hole_position >= gap and value_to_insert < x[hole_position-gap]:
                x[hole_position] = x[hole_position-gap]
                hole_position -= gap
            x[hole_position] = value_to_insert
    return x