class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_edge(self, u, v, weight):
        self.nodes.add(u)
        self.nodes.add(v)
        self.edges.append((u, v, weight))

    def get_edges(self):
        return self.edges

    def get_nodes(self):
        return list(self.nodes)