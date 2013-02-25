basic_algorithms
================

Basic algorithms in Python3


### Graph algorithms
| Name        | Performance | Space complexity |
| ------------- |:-------------:|:-------------:|
| [Breadth-first search](http://en.wikipedia.org/wiki/Breadth-first_search) ([code](./basic_algorithms/graph/bfs.py)) | O(&#124;E&#124;) | O(&#124;V&#124;) |
| [Depth-first search](http://en.wikipedia.org/wiki/Depth-first_search) ([code](./basic_algorithms/graph/dfs.py)) | O(&#124;E&#124;) | O(&#124;V&#124;) |

**Definitions:**
* V - number of nodes
* E - number of edges

Performance and space complexity are given for the worst-case scenario.


### Sorting algorithms
#### Comparison sorts
| Name        | Number of comparisons | Number of swaps | Auxiliary memory |
| ------------- |:-------------:|:-------------:|:-------------:|
| [Selection sort](http://en.wikipedia.org/wiki/Selection_sort) ([code](./basic_algorithms/sorting/selection_sort.py)) | O(n²) | O(n) | O(1) |
| [Insertion sort](http://en.wikipedia.org/wiki/Insertion_sort) ([code](./basic_algorithms/sorting/insertion_sort.py)) | O(n²) / O(n²) / O(n) | O(n²) / O(n²) / O(1) | O(1) |
| [Bubble sort](http://en.wikipedia.org/wiki/Bubble_sort) ([code](./basic_algorithms/sorting/bubble_sort.py)) | O(n²) | O(n²) / O(n²)/ O(1) | O(1) |
| [Quicksort](http://en.wikipedia.org/wiki/Quicksort) ([code](./basic_algorithms/sorting/quicksort.py)) | O(n²) / O(n log n) / O(n log n) | O(n²) / O(n log n) / O(n log n) | O(n) - naive <br/> O (n log n) - optimized |
| [Merge sort](http://en.wikipedia.org/wiki/Merge_sort) ([code](./basic_algorithms/sorting/merge_sort.py)) | O(n log n) | - | O(n) |
| [Shellsort](http://en.wikipedia.org/wiki/Shellsort) ([code](./basic_algorithms/sorting/shellsort.py)) | worst case: <br/> O(n²) with Shell's gap values <br/> O(n log² n) with Pratt's gaps | same as comparisons | O(1) |
| [Gnome sort](http://en.wikipedia.org/wiki/Gnome_sort) ([code](./basic_algorithms/sorting/gnome_sort.py)) | O(n²) / O(n²) / O(n) | O(n²) / O(n²) / O(1) | O(1) |

Number of comparisons and swaps is given for worst / average / best cases (one value if the cases are equal).

#### Non-comparison sorts
| Name        | Complexity | Auxiliary memory |
| ------------- |:-------------:|:-------------:|:-------------:|
| [Counting sort](http://en.wikipedia.org/wiki/Counting_sort) ([code](./basic_algorithms/sorting/counting_sort.py)) | O(n + k) | O(k) |


**Definitions:**
n - size of input array (list), k - maximum key value.


### Number theory algorithms
| Name        | Performance | Space complexity |
| ------------- |:-------------:|:-------------:|
| [Euclidean GCD algorithm](http://en.wikipedia.org/wiki/Euclidean_algorithm) ([code](./basic_algorithms/number_theory/gcd.py)) | O(log min(a, b)) <br/> a, b - input values | O(1) |
| [Exponentiation by squaring](http://en.wikipedia.org/wiki/Exponentiation_by_squaring) ([code](./basic_algorithms/number_theory/exp_by_squaring.py)) | O(log n) <br/> n - power | O(1) |
