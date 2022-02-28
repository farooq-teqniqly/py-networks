from teqniqly_networks.graph import Graph, MovieEdge, ActorEdge
from collections import deque

graph = Graph()


def setup_module(module):
    edges = [
        MovieEdge("The Departed", "Matt Damon", 0),
        MovieEdge("The Departed", "Jack Nicholson", 0),
        MovieEdge("The Departed", "Leonardo DiCaprio", 0),
        MovieEdge("Jackie Brown", "Samuel L. Jackson", 0),
        MovieEdge("Jackie Brown", "Robert DeNiro", 0),
        MovieEdge("The Godfather Part II", "Robert DeNiro", 0),
        MovieEdge("Fargo", "William Macy", 0),
        MovieEdge("Fargo", "Frances McDormand", 0),
        MovieEdge("Fargo", "Steve Buscemi", 0),
        MovieEdge("The Big Lebowski", "Steve Buscemi", 0),
        MovieEdge("The Big Lebowski", "John Goodman", 0),
        MovieEdge("The Big Lebowski", "Jeff Bridges", 0),
        MovieEdge("True Grit", "Jeff Bridges", 0),
        MovieEdge("True Grit", "Matt Damon", 0),
        MovieEdge("True Grit", "Josh Brolin", 0),
        MovieEdge("The Bourne Identity", "Matt Damon", 0),
        MovieEdge("The Bourne Identity", "Franka Potente", 0),
        MovieEdge("The Bourne Identity", "Julia Stiles", 0),
        ActorEdge("William Macy", "Fargo", 0),
        ActorEdge("Frances McDormand", "Fargo", 0),
        ActorEdge("Steve Buscemi", "Fargo", 0),
        ActorEdge("Steve Buscemi", "The Big Lebowski", 0),
        ActorEdge("John Goodman", "The Big Lebowski", 0),
        ActorEdge("Jeff Bridges", "The Big Lebowski", 0),
        ActorEdge("Jeff Bridges", "True Grit", 0),
        ActorEdge("Matt Damon", "True Grit", 0),
        ActorEdge("Josh Brolin", "True Grit", 0),
        ActorEdge("Matt Damon", "The Bourne Identity", 0),
        ActorEdge("Franka Potente", "The Bourne Identity", 0),
        ActorEdge("Julia Stiles", "The Bourne Identity", 0),
        ActorEdge("Samuel L. Jackson", "Jackie Brown", 0),
        ActorEdge("Robert DeNiro", "Jackie Brown", 0),
        ActorEdge("Robert DeNiro", "The Godfather Part II", 0),
        ActorEdge("Matt Damon", "The Departed", 0),
        ActorEdge("Jack Nicholson", "The Departed", 0),
        ActorEdge("Leonardo DiCaprio", "The Departed", 0)
    ]

    for edge in edges:
        graph.add_edge(edge)


def test_movie_graph():
    search_queue = deque()
    visited_nodes = []
    movie_path = []

    start_actor = "Frances McDormand"
    end_actor = "Franka Potente"

    search_queue += graph.nodes[start_actor]

    while search_queue:
        node = search_queue.popleft()
        key = node[0]

        if key in visited_nodes:
            continue

        if key != end_actor:
            search_queue += graph.nodes[key]

        visited_nodes.append(key)

        if node[2] == "m":
            movie_path.append(key)

    assert movie_path == ["Fargo", "The Big Lebowski", "True Grit", "The Bourne Identity"]
