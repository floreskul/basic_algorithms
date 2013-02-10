"""
    Breadth-first search algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Breadth-first_search
"""

def bfs(adjacent_nodes, start):
    node_queue = [start]
    visited_nodes = set([start])
    path = []
    while node_queue:
        current_node = node_queue.pop(0)
        path.append(current_node)
        for node in adjacent_nodes[current_node]:
            if node not in visited_nodes:
                visited_nodes.add(node)
                node_queue.append(node)
    return path
