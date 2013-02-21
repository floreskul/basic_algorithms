"""
    Quickselect algorithm implementation.
    It is used for finding the kth smallest number in a list,
    which is also known as kth order statistic.
    
    Description: http://pine.cs.yale.edu/pinewiki/QuickSelect
    TODO: replace with in-place version
"""

def quickselect(x, k):
    # k should start from 0
    # returns the element itself
     
    pivot = x[len(x) // 2]
    left = [e for e in x if e < pivot]
    right = [e for e in x if e > pivot]
    
    delta = len(x) - len(right)
    if k < len(left):
        return quickselect(left, k)
    elif k >= delta:
        return quickselect(right, k - delta)
    else:
        return pivot
