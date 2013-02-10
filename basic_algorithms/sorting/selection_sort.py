"""
    Selection sort algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Selection_sort
"""

def selection_sort(x):
    n = len(x)
    for i in range(n - 1):
        min_element_index = i
        for j in range(i + 1, n):
            if x[j] < x[min_element_index]:
                min_element_index = j
        x[i], x[min_element_index] = x[min_element_index], x[i]
    return x
        