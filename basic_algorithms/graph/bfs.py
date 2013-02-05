"""
    Breadth-first search algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Breadth-first_search
"""

def bfs(adjacent_nodes, start):
    queue = [start]
    visited_nodes = set([start])
    path = []
    while queue:
        current_node = queue.pop(0)
        path.append(current_node)
        for node in adjacent_nodes[current_node]:
            if node not in visited_nodes:
                visited_nodes.add(node)
                queue.append(node)
    return path
