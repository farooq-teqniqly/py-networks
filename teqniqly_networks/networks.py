from abc import ABC, abstractmethod
from typing import Any, Dict, List, Generator


class Node:
    def __init__(self, key: str, data: Any):
        self.key = key
        self.data = data


class Network(ABC):
    def __init__(self):
        self.network: Dict[str, List[Node]] = {}

    def add_node(self, key: str, data: Any):
        if self.network.get(key) is not None:
            raise ValueError(f"The node with key '{key}' already exists.")

        self.network[key] = [Node(key, data)]

    def add_edge(self, from_node_key: str, to_node_key: str):
        if not self.network.get(from_node_key):
            raise ValueError(f"The node with key '{from_node_key}' does not exist.")

        if not self.network.get(to_node_key):
            raise ValueError(f"The node with key '{to_node_key}' does not exist.")

        self.do_add_edge(from_node_key, to_node_key)

    def get_neighbors(self, key: str) -> Generator[str, None, None]:
        if not self.network.get(key):
            raise ValueError(f"The node with key '{key}' does not exist.")

        if len(self.network[key]) == 1:
            return
        else:
            for node in self.network[key][1:]:
                yield node.key

    @abstractmethod
    def do_add_edge(self, from_node_key: str, to_node_key: str):
        pass  # pragma: no cover


class DirectedNetwork(Network):
    def do_add_edge(self, from_node_key: str, to_node_key: str):
        self.network[from_node_key].append(self.network[to_node_key][0])


class UndirectedNetwork(Network):
    def do_add_edge(self, from_node_key: str, to_node_key: str):
        self.network[from_node_key].append(self.network[to_node_key][0])
        self.network[to_node_key].append(self.network[from_node_key][0])
