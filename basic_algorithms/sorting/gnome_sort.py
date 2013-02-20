"""
    Gnome sort algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Gnome_sort
    
    This algorithm is similar to the insertion sort with the difference that
    in insertion sort we just shift elements right, but here we do swapping
    as in bubble sort.
"""

def gnome_sort(x):
    n = len(x)
    pos = 1
    while pos < n:
        if x[pos-1] < x[pos]:
            pos += 1
        else:
            x[pos-1], x[pos] = x[pos], x[pos-1]
            pos = max(pos - 1, 1)
    return x
        