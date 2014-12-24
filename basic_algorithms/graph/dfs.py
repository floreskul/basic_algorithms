"""
    Depth-first search algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Depth-first_search
"""

def dfs(adjacent_nodes, start):
    node_stack = [start]
    visited_nodes = set()
    path = []
    while node_stack:
        current_node = node_stack.pop()
        if current_node not in visited_nodes:
            path.append(current_node)
            visited_nodes.add(current_node)
            for node in adjacent_nodes[current_node]:
                node_stack.append(node)
    return path
