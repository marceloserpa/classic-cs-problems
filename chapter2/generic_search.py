from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):

    def __eq__(self, other: Any) -> bool:
        ...

    def __lt__(self:C, other: C) -> bool:
        ...

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other

def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1

    while low <= high: # verify the searchable area
        mid: int = (low + high) // 2 # low + high calculate the searchable area

        if sequence[mid] < key:
            low = mid + 1 # resize the searchableare and use +1 is to skip the current element since it is not equal the searched element
        elif sequence[mid] > key:
            high = mid - 1 # the same 
        else:
            return True
    return False

def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node]:

    # frontier are places that we didnt visit yet
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))

    explored: Set[T] = { initial}

    # explore all places until reach the goal
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # if True, we found the goal
        if goal_test(current_state):
            return current_node
        
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))

    return None


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node]:

    # frontier are places that we didnt visit yet
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))

    explored: Set[T] = { initial}

    # explore all places until reach the goal
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # if True, we found the goal
        if goal_test(current_state):
            return current_node
        
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))

    return None    


def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]], heuristic: Callable[[T], float]) -> Optional[Node]:

    # frontier are places that we didnt visit yet
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))

    # places already visited
    explored: Dict[T, float] = { initial: 0.0}

    # explore all places until reach the goal
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # if True, we found the goal
        if goal_test(current_state):
            return current_node
        
        for child in successors(current_state):

            # 1 assumes a grid, need a cost function for more sophisticated apps
            new_cost: float = current_node.cost + 1

            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))

    return None    

def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]

    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    
    path.reverse()
    return path


class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop() # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


class Queue(Generic[T]):

    def __init__(self) -> None:
        self._container: Deque[T] = Deque()

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.popleft() # FIFO

    def __repr__(self) -> str:
        return repr(self._container)


class PriorityQueue(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        heappush(self._container, item)

    def pop(self) -> T:
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
        


if __name__ == "__main__":
    print(linear_contains([1,5,15,15,15,15,20], 5))
    print(binary_contains(["a", "b", "c", "d", "e"], "c"))
    print(binary_contains(["Bill Gates", "Elon Musk", "Jeff Bezos", "Marcelo Serpa", "Mark Zuckerberg"], "Marcelo Serpaa"))