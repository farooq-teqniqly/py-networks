from teqniqly_networks.graph import Graph, Edge
from collections import deque


def test_movie_graph():
    graph = Graph()

    edges = [
        Edge("Fargo", "William Macy", 0),
        Edge("Fargo", "Frances McDormand", 0),
        Edge("Fargo", "Steve Buscemi", 0),
        Edge("The Big Lebowski", "Steve Buscemi", 0),
        Edge("The Big Lebowski", "John Goodman", 0),
        Edge("The Big Lebowski", "Jeff Bridges", 0),
        Edge("True Grit", "Jeff Bridges", 0),
        Edge("True Grit", "Matt Damon", 0),
        Edge("True Grit", "Josh Brolin", 0),
        Edge("The Bourne Identity", "Matt Damon", 0),
        Edge("The Bourne Identity", "Franka Potente", 0),
        Edge("The Bourne Identity", "Julia Stiles", 0),
        Edge("William Macy", "Fargo", 0),
        Edge("Frances McDormand", "Fargo", 0),
        Edge("Steve Buscemi", "Fargo", 0),
        Edge("Steve Buscemi", "The Big Lebowski", 0),
        Edge("John Goodman", "The Big Lebowski", 0),
        Edge("Jeff Bridges", "The Big Lebowski", 0),
        Edge("Jeff Bridges", "True Grit", 0),
        Edge("Matt Damon", "True Grit", 0),
        Edge("Josh Brolin", "True Grit", 0),
        Edge("Matt Damon", "The Bourne Identity", 0),
        Edge("Franka Potente", "The Bourne Identity", 0),
        Edge("Julia Stiles", "The Bourne Identity", 0)
    ]

    for edge in edges:
        graph.add_edge(edge)

    search_queue = deque()
    visited_nodes = []

    start_actor = "William Macy"
    end_actor = "Julia Stiles"

    search_queue += graph.nodes[start_actor]

    while search_queue:
        node = search_queue.popleft()
        key = node[0]

        if key in visited_nodes:
            continue

        if key != end_actor:
            search_queue += graph.nodes[key]

        visited_nodes.append(key)

    pass
