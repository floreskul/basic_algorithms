"""
    Insertion sort algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Insertion_sort
"""

def insertion_sort(x):
    n = len(x)
    # elements [0:i-1] are sorted
    for i in range(1, n):
        value_to_insert = x[i]
        hole_position = i
        # shift elements right until there is found the right place
        while hole_position > 0 and value_to_insert < x[hole_position-1]:
            x[hole_position] = x[hole_position - 1]
            hole_position -= 1
        x[hole_position] = value_to_insert
    return x
        