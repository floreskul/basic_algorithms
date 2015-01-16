"""
    Kadane's algorithm implementation.
    It solves the maximum subarray problem - the task of finding the contiguous
    subarray within an array of numbers of the largest sum.
    
    Description: http://en.wikipedia.org/wiki/Maximum_subarray_problem
"""

def kadanes_max_subarray(a):
    max_ending_here = current_max = 0
    start, end = best_start, best_end = 0, 0

    for i, x in enumerate(a):
        # at every point we either append current element
        # or start a new array from the current element
        if max_ending_here + x > 0:
            max_ending_here += x
            end = i + 1
        else:
            max_ending_here = 0
            start = i + 1

        # update best known result if needed
        if max_ending_here > current_max:
            current_max = max_ending_here
            best_start, best_end = start, end
    return a[best_start:best_end]
