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
| Name        | Number of comparisons | Number of swaps | Auxiliary memory |
| ------------- |:-------------:|:-------------:|:-------------:|
| [Selection sort](http://en.wikipedia.org/wiki/Selection_sort) ([code](./basic_algorithms/sorting/selection_sort.py)) | O(n²) | O(n) | O(1) |
| [Insertion sort](http://en.wikipedia.org/wiki/Insertion_sort) ([code](./basic_algorithms/sorting/insertion_sort.py)) | O(n²) / O(n²) / O(n) | O(n²) / O(n²) / O(1) | O(1) |
| [Bubble sort](http://en.wikipedia.org/wiki/Bubble_sort) ([code](./basic_algorithms/sorting/bubble_sort.py)) | O(n²) | O(n²) | O(1) |
| [Quicksort](http://en.wikipedia.org/wiki/Quicksort) ([code](./basic_algorithms/sorting/quicksort.py)) | O(n²) / O(n log n) / O(n log n) | O(n²) / O(n log n) / O(n log n) | O(n) - naive <br/> O (n log n) - optimized |
| [Merge sort](http://en.wikipedia.org/wiki/Merge_sort) ([code](./basic_algorithms/sorting/merge_sort.py)) | O(n log n) | - | O(n) |


**Definitions:**
n - size of input array (list)

Number of comparisons and swaps is given for worst / average / best cases (one value if the cases are equal).
