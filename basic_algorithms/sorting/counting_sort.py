"""
    Counting sort algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Counting_sort
    Possible improvement: add and process min_value as a parameter
"""

def counting_sort(x, max_value):
    n = len(x)
    m = (max_value + 1)
    count = [0] * m
    for v in x:
        count[v] += 1
    i = 0
    for v in range(m):
        # add count[v] copies of v to the array
        for c in range(count[v]):
            x[i] = v
            i += 1
    return x
        