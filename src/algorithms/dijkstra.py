import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph.get_nodes()}
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        for u, v, w in graph.get_edges():
            if u == node:
                neighbor = v
            elif v == node:
                neighbor = u
            else:
                continue

            new_dist = current_dist + w

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist