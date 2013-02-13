"""
    Merge sort algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Merge_sort
"""

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(x):
    n = len(x)
    if n <= 1:
        return x
    left = merge_sort(x[:n/2])
    right =  merge_sort(x[n/2:])
    return merge(left, right)
