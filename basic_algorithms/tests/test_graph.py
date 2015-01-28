import copy
import unittest
from ..graph.bfs import bfs
from ..graph.dfs import dfs
from ..graph.topological_sort import topological_sort

class TestGraphAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.bfs_graph1 = {
            1: [2, 3],
            2: [1, 4, 5],
            3: [1],
            4: [2],
            5: [2]
        }
        self.bfs_graph2 = {
            'a': ['b', 'c'],
            'b': ['d', 'e'],
            'c': ['g'],
            'd': ['f'],
            'e': ['f'],
            'f': [],
            'g': []
        }
        self.spanning_tree_graph = {
            'a': {'b': 1, 'd': 4, 'e': 3},
            'b': {'a': 1, 'd': 4, 'e': 2},
            'c': {'e': 4, 'f': 5},
            'd': {'a': 4, 'b': 4, 'e': 4},
            'e': {'a': 3, 'b': 4, 'd': 4, 'f': 7},
            'f': {'c': 5, 'e': 7}
        }

        self.topological_sort_cyclic_graph = {
            'a': ['b'],
            'b': ['c'],
            'c': ['a']
        }

        self.topological_sort_graph = {
            2: [],
            3: [8, 10],
            5: [11],
            7: [8, 11],
            8: [9],
            9: [],
            10: [],
            11: [2, 9, 10]
        }
        
    
    def test_bfs(self):
        self.assertEqual(bfs(self.bfs_graph1, 1), [1, 2, 3, 4, 5])
        self.assertEqual(bfs(self.bfs_graph2, 'a'), ['a', 'b', 'c', 'd', 'e', 'g', 'f'])
        
    def test_dfs(self):
        self.assertEqual(dfs(self.bfs_graph1, 1), [1, 3, 2, 5, 4])
        self.assertEqual(dfs(self.bfs_graph2, 'a'), ['a', 'c', 'g', 'b', 'e', 'f', 'd'])

    def test_topological_sort(self):
        # test cyclic graph case
        graph = copy.deepcopy(self.topological_sort_cyclic_graph)
        result = topological_sort(graph)
        self.assertTrue(result is None)

        # test normal case
        graph = copy.deepcopy(self.topological_sort_graph)
        result = topological_sort(graph)
        self.assertTrue(len(result), 8)
        
        # check topological order
        for u in self.topological_sort_graph:
            for v in self.topological_sort_graph[u]:
                self.assertTrue(result.index(u) < result.index(v))
    
    # def test_minimum_spanning_tree(self, algorithm):
    #     tree = algorithm(self.spanning_tree_graph)
        
    #     edge_count = len([(u, v) for u in tree for v in tree[u]])
    #     self.assertEqual(edge_count, len(self.spanning_tree_graph) - 1,
    #                      "Tree should have |V|-1 edges")
        
    #     tree_adjacency_graph = {u: tree[u].keys() for u in tree}
    #     component = bfs(tree_adjacency_graph, 'a')
    #     self.assertEqual(len(component), len(self.spanning_tree_graph),
    #                      "Spanning tree should connect all nodes")
        
    #     total_weight = sum([tree[u][v] for u in tree for v in tree[u]]) / 2
    #     self.assertEqual(total_weight, 16,
    #                      "Spanning tree should be minimum-cost subgraph")
