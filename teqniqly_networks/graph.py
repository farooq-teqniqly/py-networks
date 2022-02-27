from typing import List, Any, Dict, Tuple


class Edge:
    def __init__(self, node1, node2, weight: int):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight


class Graph:
    def __init__(self):
        self.nodes: Dict[Any, List[Tuple[Any, int]]] = {}

    def add_edge(self, edge):
        if edge.node1 not in self.nodes:
            self.nodes[edge.node1] = []

        if edge.node2 not in self.nodes:
            self.nodes[edge.node2] = []

        self.nodes[edge.node1].append((edge.node2, edge.weight))

        # uncomment for undirected graph
        # self.nodes[edge.node2].append((edge.node1, edge.weight))
