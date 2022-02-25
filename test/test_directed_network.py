from teqniqly_networks.networks import DirectedNetwork

network = DirectedNetwork()


def setup_function(function):
    network.add_node("me", {"name": "Farooq", "age": 44})
    network.add_node("alice", {"name": "Alice", "age": 35})
    network.add_node("bob", {"name": "Bob", "age": 56})
    network.add_node("claire", {"name": "Claire", "age": 42})
    network.add_node("peggy", {"name": "Peggy", "age": 60})
    network.add_node("thom", {"name": "Thom", "age": 44})
    network.add_node("jonny", {"name": "Jonny", "age": 29})
    network.add_node("anuj", {"name": "Anuj", "age": 46})

    network.add_edge("me", "bob")
    network.add_edge("me", "claire")
    network.add_edge("me", "alice")
    network.add_edge("bob", "anuj")
    network.add_edge("bob", "peggy")
    network.add_edge("alice", "peggy")
    network.add_edge("claire", "jonny")
    network.add_edge("claire", "thom")


def test_can_get_neighbors():
    assert list(network.get_neighbors("me")) == ["bob", "claire", "alice"]
    assert list(network.get_neighbors("bob")) == ["anuj", "peggy"]
    assert list(network.get_neighbors("alice")) == ["peggy"]
    assert list(network.get_neighbors("claire")) == ["jonny", "thom"]

    people_without_neighbors = ["anuj", "peggy", "jonny", "thom"]

    for person in people_without_neighbors:
        assert len(list(network.get_neighbors(person))) == 0
