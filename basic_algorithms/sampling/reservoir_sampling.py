"""
    Reservoir sampling algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Reservoir_sampling
"""
import random

def reservoir_sampling(x, k):
	reservoir = []

	# fill the reservoir with first k elements
	for i in range(k):
		reservoir.append(x[i])

	# replace elements with gradually decreasing probability
	for i in range(k, len(x)):
		# choose an index within inclusive range
		j = random.randint(1, i)
		if j < k:
			reservoir[j] = x[i]

	return reservoir