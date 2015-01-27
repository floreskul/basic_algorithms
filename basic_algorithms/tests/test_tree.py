import unittest
import collections

from ..tree.traversal import pre_order, in_order, post_order, level_order

Node = collections.namedtuple('Node', ['value', 'left', 'right'])


class TestTreeAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.tree = Node(
            'f',
            Node(
                'b',
                Node(
                    'a',
                    None,
                    None
                ),
                Node(
                    'd',
                    Node(
                        'c',
                        None,
                        None
                    ),
                    Node(
                        'e',
                        None,
                        None
                    )
                )
            ),
            Node(
                'g',
                None,
                Node(
                    'i',
                    Node(
                        'h',
                        None,
                        None
                    ),
                    None
                )
            )
        )
        
    
    def test_pre_order(self):
        self.assertEqual(pre_order(self.tree), ['f', 'b', 'a', 'd', 'c', 'e', 'g', 'i', 'h'])

    def test_in_order(self):
        self.assertEqual(in_order(self.tree), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

    def test_post_order(self):
        self.assertEqual(post_order(self.tree), ['a', 'c', 'e', 'd', 'b', 'h', 'i', 'g', 'f'])

    def test_level_order(self):
        self.assertEqual(level_order(self.tree), ['f', 'b', 'g', 'a', 'd', 'i', 'c', 'e', 'h'])
