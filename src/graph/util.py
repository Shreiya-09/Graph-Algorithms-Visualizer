def load_graph_from_edges(edge_list):
    """
    Create graph from list of edges
    edge_list = [(u, v, w), ...]
    """
    from graph.graph import Graph

    g = Graph()
    for u, v, w in edge_list:
        g.add_edge(u, v, w)
    return g


def calculate_total_weight(edges):
    """
    Calculate total weight of MST
    """
    return sum([w for _, _, w in edges])


def print_mst(mst):
    """
    Nicely print MST edges
    """
    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} -- {v} (weight {w})")