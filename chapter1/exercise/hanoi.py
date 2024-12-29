
from typing import TypeVar, Generic, List

T = TypeVar("T")

class Stack(Generic[T]):

    def __init__(self, name: str) -> None:
        self._container: List[T] = []
        self._name = name

    def push(self, item: T) -> None:
        print(f'tower = {self._name} push = {item}')
        self._container.append(item)

    def pop(self) -> T:
        item: int = self._container.pop()
        print(f'tower = {self._name} pop = {item}')
        return item

    # this is what will be printed when the print method being invoked
    def __repr__(self) -> str:
        return repr(self._container)

    def print(self) -> None:
        print(f'tower = {self._name}')

        if len(self._container) <= 0:
            print("Empty")
        else:
            for disk in self._container:
                print(disk)


class HanoiTowerSolver:

    def __init__(self, disks: int) -> None:
        self._disks: int = disks
        self._towers: List[Stack[int]] = []
        self._towers.append(Stack("A"))
        self._towers.append(Stack("B"))
        self._towers.append(Stack("C"))

    def move_disk(self, source: Stack[int], destination: Stack[int], auxiliar: Stack[int], n: int) -> None:
        if n == 1:
            destination.push(source.pop())
        else:
            self.move_disk(source, auxiliar, destination, n - 1)
            self.move_disk(source, destination, auxiliar, 1)
            self.move_disk(auxiliar, destination , source, n -1 )

    def solve(self) -> None:
        for i in range(1, self._disks + 1):
            self._towers[0].push(i)
        self.move_disk(self._towers[0], self._towers[2], self._towers[1], self._disks)        

    def print(self) -> None:
        for tower in self._towers:
            tower.print()

    

if __name__ == "__main__":

    num_discs :int = 3
    hanoiTowerSolver: HanoiTowerSolver = HanoiTowerSolver(3)
    hanoiTowerSolver.solve()

    print("---------")
    hanoiTowerSolver.print()
