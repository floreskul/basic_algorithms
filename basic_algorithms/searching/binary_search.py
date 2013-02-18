"""
    Binary search algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Binary_search
"""
import random

def binary_search(x, key):
    print(x, key)
    left = 0
    right = len(x) - 1
    while left <= right:
        middle = (left + right) // 2
        print (middle, left, right)
        if x[middle] < key:
            left = middle + 1
        elif x[middle] > key:
            right = middle - 1
        else:
            return middle
    return None
