import heapq

def prim(graph, start):
    visited = set()
    mst = []
    pq = [(0, start, None)]  # (weight, current_node, parent)

    while pq:
        weight, node, parent = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if parent is not None:
            mst.append((parent, node, weight))

        for u, v, w in graph.get_edges():
            if u == node and v not in visited:
                heapq.heappush(pq, (w, v, node))
            elif v == node and u not in visited:
                heapq.heappush(pq, (w, u, node))

    return mst