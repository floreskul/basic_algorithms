"""
    Knuth (Fisher-Yates) shuffle algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
"""
import random

def knuth_shuffle(x):
    for i in range(len(x) - 1, -1, -1):
        j = random.randint(0, i)
        x[i], x[j] = x[j], x[i]
    return x
