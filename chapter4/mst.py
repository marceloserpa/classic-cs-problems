from optparse import Option
from typing import TypeVar, List, Optional
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue

V = TypeVar('V')
WeightedPath = List[WeightedEdge] 

def total_weight(wp: WeightedPath) -> float:
    return sum([e.weight for e in wp])


def mst(wg: WeightedGraph[V], start: int = 0) -> Optional[WeightedPath]:

    if start > (wg.vertex_count - 1) or start < 0:
        return None

    result: WeightedPath = [] #holds the final MST
    pq: PriorityQueue[WeightedEdge] = PriorityQueue()
    visited: List[bool] = [False] * wg.vertex_count

    def visit(index: int):
        visited[index] = True
        for edge in wg.edges_for_index(index):
            # add all edges coming from here to PQ
            if not visited[edge.v]:
                pq.push(edge)
    # the first vertex is where everything begins
    visit(start)

    while not pq.empty:
        edge = pq.pop()

        if visited[edge.v]:
            continue # don't ever revisit

        result.append(edge)
        visit(edge.v)

    return result

def print_weighted_path(wg: WeightedGraph, wp: WeightedPath) -> None:
    for edge in wp:
        print(f"{wg.vertex_at(edge.u)} {edge.weight}> {wg.vertex_at(edge.v)}")
        print(f"Total Weight: {total_weight(wp)}")   


