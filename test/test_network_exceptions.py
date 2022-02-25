from typing import Optional

import pytest

from teqniqly_networks.networks import Network


class TestNetwork(Network):

    def do_add_edge(self, from_node_key: str, to_node_key: str):
        pass # pragma: no cover


network: Optional[TestNetwork] = None


def setup_function(function):
    global network
    network = TestNetwork()
    network.add_node("foo", {})
    network.add_node("bar", {})


def test_add_node_when_node_exists_raises_exception():
    with pytest.raises(ValueError) as error:
        network.add_node("foo", {})

    assert str(error.value) == "The node with key 'foo' already exists."


@pytest.mark.parametrize("from_node", [None, "", "  "])
def test_add_edge_when_from_node_not_specified_raises_exception(from_node):
    with pytest.raises(ValueError) as error:
        network.add_edge(from_node, "foo")

    assert str(error.value) == "The 'from_node_key' parameter must be a non-empty string."


def test_add_edge_when_from_node_does_not_exist_raises_exception():
    with pytest.raises(ValueError) as error:
        network.add_edge("baz", "foo")

    assert str(error.value) == "The node with key 'baz' does not exist."


@pytest.mark.parametrize("to_node", [None, "", "  "])
def test_add_edge_when_to_node_not_specified_raises_exception(to_node):
    with pytest.raises(ValueError) as error:
        network.add_edge("foo", to_node)

    assert str(error.value) == "The 'to_node_key' parameter must be a non-empty string."


def test_add_edge_when_to_node_does_not_exist_raises_exception():
    with pytest.raises(ValueError) as error:
        network.add_edge("foo", "qux")

    assert str(error.value) == "The node with key 'qux' does not exist."


def test_get_neighbors_when_node_does_not_exist_raises_exception():
    with pytest.raises(ValueError) as error:
        list(network.get_neighbors("qux"))

    assert str(error.value) == "The node with key 'qux' does not exist."
