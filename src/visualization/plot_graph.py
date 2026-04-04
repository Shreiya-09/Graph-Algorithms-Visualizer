import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, mst_edges=None):
    G = nx.Graph()

    for u, v, w in graph.get_edges():
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    if mst_edges:
        nx.draw_networkx_edges(
            G, pos,
            edgelist=[(u, v) for u, v, w in mst_edges],
            width=3
        )

    plt.show()