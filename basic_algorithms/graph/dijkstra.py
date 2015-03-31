"""
    Dijkstra's algorithm implementation.
    Description: http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""


def dijkstra_basic(graph, source):
    processed_nodes = set([source])
    distances = {node: float('inf') for node in graph.keys()}
    distances[source] = 0

    while processed_nodes != graph.keys():
        best_edge = None
        for u, edges in graph.items():
            for v, weight in edges:
                if u in processed_nodes and v not in processed_nodes:

                    if best_edge is None or \
                            best_edge[2] > (distances[u] + weight):
                        best_edge = u, v, (distances[u] + weight)
        if not best_edge:
            break
        u, v, d = best_edge
        distances[v] = d
        processed_nodes.add(v)
    return distances
