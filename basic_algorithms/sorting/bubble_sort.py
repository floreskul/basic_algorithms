"""
    Bubble sort algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Bubble_sort
    Possible optimization: stop if nothing is swapped during the iteration
"""

def bubble_sort(x):
    n = len(x)
    # elements [n-k-1:n] are sorted
    for k in range(n):
        for i in range(1, n):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
    return x
