Basic Algorithms
================

Collection of classic algorithms implemented in Python3.


### Graph algorithms
| Name        | Performance | Space complexity |
| ------------- |:-------------:|:-------------:|
| [Breadth-first search](./basic_algorithms/graph/bfs.py) ([wiki](http://en.wikipedia.org/wiki/Breadth-first_search)) | O(&#124;E&#124;) | O(&#124;V&#124;) |
| [Depth-first search](./basic_algorithms/graph/dfs.py) ([wiki](http://en.wikipedia.org/wiki/Depth-first_search)) | O(&#124;E&#124;) | O(&#124;V&#124;) |

**Definitions:**
* V - number of nodes
* E - number of edges

Performance and space complexity are given for the worst-case scenario.


### Sorting algorithms
#### Comparison sorts
| Name        | Number of comparisons | Number of swaps | Auxiliary memory |
| ------------- |:-------------:|:-------------:|:-------------:|
| [Selection sort](./basic_algorithms/sorting/selection_sort.py) ([wiki](http://en.wikipedia.org/wiki/Selection_sort)) | O(n²) | O(n) | O(1) |
| [Insertion sort](./basic_algorithms/sorting/insertion_sort.py) ([wiki](http://en.wikipedia.org/wiki/Insertion_sort)) | O(n²) / O(n²) / O(n) | O(n²) / O(n²) / O(1) | O(1) |
| [Bubble sort](./basic_algorithms/sorting/bubble_sort.py) ([wiki](http://en.wikipedia.org/wiki/Bubble_sort)) | O(n²) | O(n²) / O(n²)/ O(1) | O(1) |
| [Quicksort](./basic_algorithms/sorting/quicksort.py) ([wiki](http://en.wikipedia.org/wiki/Quicksort)) | O(n²) / O(n log n) / O(n log n) | O(n²) / O(n log n) / O(n log n) | O(n) - naive <br/> O (n log n) - optimized |
| [Merge sort](./basic_algorithms/sorting/merge_sort.py) ([wiki](http://en.wikipedia.org/wiki/Merge_sort)) | O(n log n) | - | O(n) |
| [Shellsort](./basic_algorithms/sorting/shellsort.py) ([wiki](http://en.wikipedia.org/wiki/Shellsort)) | worst case: <br/> O(n²) with Shell's gap values <br/> O(n log² n) with Pratt's gaps | same as comparisons | O(1) |
| [Gnome sort](./basic_algorithms/sorting/gnome_sort.py) ([wiki](http://en.wikipedia.org/wiki/Gnome_sort)) | O(n²) / O(n²) / O(n) | O(n²) / O(n²) / O(1) | O(1) |

Number of comparisons and swaps is given for worst / average / best cases (one value if the cases are equal).

#### Non-comparison sorts
| Name        | Complexity | Auxiliary memory |
| ------------- |:-------------:|:-------------:|:-------------:|
| [Counting sort](./basic_algorithms/sorting/counting_sort.py) ([wiki](http://en.wikipedia.org/wiki/Counting_sort)) | O(n + k) | O(k) |


**Definitions:**
n - size of input array (list), k - maximum key value.


### Search algorithms
| Name        | Performance | Space complexity |
| ------------- |:-------------:|:-------------:|
| [Binary search](./basic_algorithms/searching/binary_search.py) ([wiki](http://en.wikipedia.org/wiki/Binary_search)) | O(log n) | O(1) |
| [Quickselect](./basic_algorithms/searching/quickselect.py) ([wiki](http://en.wikipedia.org/wiki/Selection_algorithm)) | O(log n) | O(1) |
| [Kadane's maximum subarray algorithm](./basic_algorithms/searching/kadane.py) ([wiki](http://en.wikipedia.org/wiki/Maximum_subarray_problem)) | O(n) | O(1) |


### Sampling algorithms
| Name        | Performance | Space complexity |
| ------------- |:-------------:|:-------------:|
| [Reservoir sampling](./basic_algorithms/sampling/reservoir_sampling.py) ([wiki](http://en.wikipedia.org/wiki/Reservoir_sampling)) | O(n) | O(k) <br/> k - sample size |


### Number theory algorithms
| Name        | Performance | Space complexity |
| ------------- |:-------------:|:-------------:|
| [Euclidean GCD algorithm](./basic_algorithms/number_theory/gcd.py) ([wiki](http://en.wikipedia.org/wiki/Euclidean_algorithm)) | O(log min(a, b)) <br/> a, b - input values | O(1) |
| [Exponentiation by squaring](./basic_algorithms/number_theory/exp_by_squaring.py) ([wiki](http://en.wikipedia.org/wiki/Exponentiation_by_squaring)) | O(log n) <br/> n - power | O(1) |
| [Sieve of Eratosthenes](./basic_algorithms/number_theory/sieve_of_eratosthenes.py) ([wiki](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)) | O(n log log n) <br/> n - upper limit | O(n) |
| [Karatsuba multiplication algorithm](./basic_algorithms/number_theory/karatsuba.py) ([wiki](http://en.wikipedia.org/wiki/Karatsuba_algorithm)) | O(n ^ 1.585) <br/> n - number of digits | O(1) |
