from graph.graph import Graph
from algorithms.prim import prim
from algorithms.dijkstra import dijkstra
from algorithms.kruskal import kruskal
from visualization.plot_graph import draw_graph

def main():
    g = Graph()

    # Sample Graph
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 1)
    g.add_edge(3, 2, 2)
    g.add_edge(2, 4, 1)
    g.add_edge(3, 4, 5)

    print("Shortest Paths from Node 1:")
    print(dijkstra(g, 1))

    print("\nMinimum Spanning Tree (Kruskal):")
    mst = kruskal(g)
    print(mst)

    draw_graph(g, mst)

    print("\nMinimum Spanning Tree (Prim):")
    mst_prim = prim(g, 1)
    print(mst_prim)

if __name__ == "__main__":
    main()