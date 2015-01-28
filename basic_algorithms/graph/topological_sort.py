"""
    Topological sort (by Kahn) algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Topological_sorting
"""

def _get_reversed_graph(adjacent_nodes):
    reversed_graph = {u: [] for u in adjacent_nodes}
    for u in adjacent_nodes:
        for v in adjacent_nodes[u]:
            reversed_graph[v].append(u)
    return reversed_graph

def topological_sort(adjacent_nodes):
    result = []
    reversed_graph = _get_reversed_graph(adjacent_nodes)

    no_incoming_edge_nodes = [u for u in reversed_graph if not reversed_graph[u]]

    while no_incoming_edge_nodes:
        current_node = no_incoming_edge_nodes.pop(len(no_incoming_edge_nodes) - 1)
        result.append(current_node)

        # iterate the copy of the list in order to be able to remove elements
        for node in adjacent_nodes[current_node][:]:
            # remove the "current_node -> node" edge
            adjacent_nodes[current_node].remove(node)
            reversed_graph[node].remove(current_node)
            if not reversed_graph[node]:
                no_incoming_edge_nodes.append(node)

    # return an error if there still are edges in the graph
    if any(adjacent_nodes.values()):
        return None
    return result

