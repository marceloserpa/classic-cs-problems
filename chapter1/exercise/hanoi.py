
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
        self._moves: int = 0

    def move_disk(self, source: Stack[int], destination: Stack[int], auxiliar_towers: List[Stack[int]], n: int) -> None:
        print(f'#move = {self._moves} source = {source} destination = {destination} aux-towers = {auxiliar_towers}')
        
        
        self._moves += 1
        if n == 1:
            destination.push(source.pop())

        if n != 1 and len(auxiliar_towers) == 1:
            self.move_disk(source, auxiliar_towers[0], [destination], n - 1)
            
            self.move_disk(source, destination, auxiliar_towers, 1)
            
            self.move_disk(auxiliar_towers[0], destination , [source], n -1 )


    def solve(self) -> None:
        for i in range(1, self._disks + 1):
            self._towers[0].push(i)

        source_tower: Stack[int] = self._towers[0]
        dest_tower: Stack[int] = self._towers[-1:][0] # extract a list with only the last item and get the first element from the new list
        aux_towers: List[Stack[int]] = self._towers[1:-1] # create new list without the first and the last element

        self.move_disk(source_tower, dest_tower, aux_towers, self._disks)        

    def print(self) -> None:
        print(f'total moves = {self._moves}')

        for tower in self._towers:
            tower.print()

    

if __name__ == "__main__":

    hanoiTowerSolver: HanoiTowerSolver = HanoiTowerSolver(3)
    hanoiTowerSolver.solve()

    print("---------")
    hanoiTowerSolver.print()
