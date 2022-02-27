import os
from teqniqly_networks.graph import Edge, Graph

graph = Graph()


def create_graph_from_file():
    with open(os.path.join(os.getcwd(), "files", "cities.tsv")) as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        weights = [int(ln.strip()) for ln in line.split(' ') if len(ln) > 0]

        for j, weight in enumerate(weights):
            if j == i:
                continue

            graph.add_edge(Edge(f"c{i}", f"c{j}", weight))


def setup_module(module):
    create_graph_from_file()


def test_graph_creation():
    assert len(graph.nodes) == 42

    for key in graph.nodes.keys():
        assert len(graph.nodes[key]) == 41
