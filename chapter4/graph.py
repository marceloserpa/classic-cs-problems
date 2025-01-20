from typing import Optional
from typing import TypeVar, Generic, List, Optional
from edge import Edge

# type of the vertices in the graph
V = TypeVar("V")

class Graph(Generic[V]):

    def __init__(self, vertices: List[V] = []) -> None:
        self._variables: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]