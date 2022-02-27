from typing import List, Any, Dict, Tuple
from collections import deque


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


def tsp_nna(graph: Graph, start_node) -> deque:
    unvisited_nodes = [key for key in graph.nodes.keys() if key != start_node]
    tour = deque()
    current_node = start_node
    tour.append(current_node)

    while len(unvisited_nodes) > 0:
        next_node = _find_nn(graph.nodes[current_node], unvisited_nodes, start_node)
        tour.append(next_node)
        unvisited_nodes.remove(next_node[0])
        current_node = next_node[0]
        pass

    tour.append((start_node, [tup for tup in graph.nodes[current_node] if tup[0] == start_node][0][1]))

    return tour


def _find_nn(node: List[Tuple[Any, int]], unvisited_nodes: list, start_node) -> Tuple[Any, int]:
    nn = (None, 1000000)

    for neighbor in node:
        if neighbor[0] == start_node:
            continue

        if neighbor[0] not in unvisited_nodes:
            continue

        if neighbor[1] < nn[1]:
            nn = neighbor

    return nn
