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



if __name__ == "__main__":
    print(linear_contains([1,5,15,15,15,15,20], 5))
    print(binary_contains(["a", "b", "c", "d", "e"], "c"))
    print(binary_contains(["Bill Gates", "Elon Musk", "Jeff Bezos", "Marcelo Serpa", "Mark Zuckerberg"], "Marcelo Serpaa"))