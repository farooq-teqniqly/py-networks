from typing import List

from teqniqly_networks.graph import Edge, Graph


def test_graph():
    edges: List[Edge] = [Edge("me", "bob", 0),
                         Edge("me", "claire", 0),
                         Edge("me", "alice", 0),
                         Edge("bob", "anuj", 0),
                         Edge("bob", "peggy", 0),
                         Edge("alice", "peggy", 0),
                         Edge("claire", "jonny", 0),
                         Edge("claire", "thom", 0)]

    graph = Graph()

    for edge in edges:
        graph.add_edge(edge)

    pass
