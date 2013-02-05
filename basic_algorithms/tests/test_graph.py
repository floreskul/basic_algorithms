import unittest
from ..graph.bfs import bfs
from ..graph.dfs import dfs

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.adjacent_nodes = {
                          1: [2, 3],
                          2: [1, 4, 5],
                          3: [1],
                          4: [2],
                          5: [2]
                          }
    
    def test_bfs(self):
        self.assertEqual(bfs(self.adjacent_nodes, 1), [1, 2, 3, 4, 5])
        
    def test_dfs(self):
        self.assertEqual(dfs(self.adjacent_nodes, 1), [1, 3, 2, 5, 4])