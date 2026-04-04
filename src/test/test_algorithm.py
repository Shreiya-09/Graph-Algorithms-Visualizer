from graph.graph import Graph
from algorithms.dijkstra import dijkstra
from algorithms.kruskal import kruskal
from algorithms.prim import prim


def create_sample_graph():
    g = Graph()
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 1)
    g.add_edge(3, 2, 2)
    g.add_edge(2, 4, 1)
    g.add_edge(3, 4, 5)
    return g


# ✅ Test Dijkstra
def test_dijkstra():
    g = create_sample_graph()
    result = dijkstra(g, 1)

    expected = {
        1: 0,
        2: 3,
        3: 1,
        4: 4
    }

    assert result == expected
    print("Dijkstra Test Passed ✅")


# ✅ Test Kruskal
def test_kruskal():
    g = create_sample_graph()
    mst = kruskal(g)

    total_weight = sum([w for _, _, w in mst])

    assert total_weight == 4
    print("Kruskal Test Passed ✅")


# ✅ Test Prim
def test_prim():
    g = create_sample_graph()
    mst = prim(g, 1)

    total_weight = sum([w for _, _, w in mst])

    assert total_weight == 4
    print("Prim Test Passed ✅")


if __name__ == "__main__":
    test_dijkstra()
    test_kruskal()
    test_prim()