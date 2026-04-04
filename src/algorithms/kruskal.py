def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

def kruskal(graph):
    result = []
    i, e = 0, 0

    edges = sorted(graph.get_edges(), key=lambda x: x[2])
    parent = {}
    rank = {}

    for node in graph.get_nodes():
        parent[node] = node
        rank[node] = 0

    while e < len(graph.get_nodes()) - 1:
        u, v, w = edges[i]
        i += 1

        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)

    return result