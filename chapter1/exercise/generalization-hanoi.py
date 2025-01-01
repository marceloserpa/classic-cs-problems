
from typing import TypeVar, Generic, List

T = TypeVar("T")

class Stack(Generic[T]):

    def __init__(self, name: str) -> None:
        self._container: List[T] = []
        self._name = name

    def push(self, item: T) -> None:
        #print(f'tower = {self._name} push = {item}')
        self._container.append(item)

    def pop(self) -> T:
        item: int = self._container.pop()
        #print(f'tower = {self._name} pop = {item}')
        return item

    def get(self, index: int) -> int:
        return self._container[index]

    def get_size(self) -> int:
        return len(self._container)        

    def is_not_empty(self) -> bool :

        return len(self._container) > 0

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

    def __init__(self, disks: int, number_of_towers: int) -> None:
        self._disks: int = disks
        self._moves: int = 0

        self._towers: List[Stack[int]] = [Stack(f"T{i}") for i in range(number_of_towers)]
        for i in range(1, self._disks + 1):
            self._towers[0].push(i) 

    def frame_stewart(self, source: int, destination: int, auxiliary: List[int], number_of_disks: int, number_of_towers: int ) -> None:
        # Solves the generalized Tower of Hanoi problem using a fixed partition size (n // 2).

        # Base case: If there's only one disk, move it directly.
        if number_of_disks == 1:
            # Move the disk from source to destination
            disk: int = self._towers[source].pop()
            self._towers[destination].push(disk)
            self._moves += 1
            print(f'move disk {disk}: {source} => {destination}')
            self.print()
            return 1

        # Define partition size: m = n // 2
        partition = number_of_disks // 2

        # Partition the problem into three stages.
        self.frame_stewart(source, auxiliary[0], [destination] + auxiliary[1:], partition, number_of_towers)
        self.frame_stewart(source, destination, auxiliary[1:], number_of_disks - partition, number_of_towers - 1)
        self.frame_stewart(auxiliary[0], destination, [source] + auxiliary[1:], partition, number_of_towers)
       

    def print(self) -> None:
        j: int = self._disks-1 

        report: str = ""
        for _ in range(self._disks):
            for tower in self._towers:
                
                tower_size: int = tower.get_size() 

                if (tower_size - 1) >= j:
                    report += " " + str(tower.get(j)) + " "
                else:
                    report += " X "

            j -= 1
            report += "\n"

        print(report)

    def solve(self) -> None:

        self.print()
        
        self.frame_stewart(0, 4, [1,2], self._disks, 4)
    

if __name__ == "__main__":

    hanoiTowerSolver: HanoiTowerSolver = HanoiTowerSolver(4, 5)

    hanoiTowerSolver.solve()

    print("---------")
    
