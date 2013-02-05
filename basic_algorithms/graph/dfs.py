"""
    Depth-first search algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Depth-first_search
"""

def dfs(adjacent_nodes, start):
    stack = [start]
    visited_nodes = set([start])
    path = []
    while stack:
        current_node = stack.pop()
        path.append(current_node)
        for node in adjacent_nodes[current_node]:
            if node not in visited_nodes:
                visited_nodes.add(node)
                stack.append(node)
    return path
