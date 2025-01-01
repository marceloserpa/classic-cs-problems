
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

    def __init__(self, disks: int) -> None:
        self._disks: int = disks
        self._towers: List[Stack[int]] = []
        self._towers.append(Stack("A"))
        self._towers.append(Stack("B"))
        self._towers.append(Stack("C"))
        self._moves: int = 0

    def move_disk(self, source: int, destination: int, aux: int, n: int) -> None:
        #print(f'#move = {self._moves} disk = {n} source = {source} destination = {destination} aux-towers = {aux}')

        # TODO: just for testing
        if(self._moves > 20):
             raise Exception("It doesnt make sense")     

        if len(self._towers) < 3:
            raise Exception("Invalid number of towers, the minimum is 3")   
        
        self._moves += 1
        if n == 1:
            self._towers[destination].push(self._towers[source].pop())
            self.print()
            return None

        if len(self._towers) == 3:
            self.move_disk(source, aux, destination, n - 1)
            
            self.move_disk(source, destination, aux, 1)
            
            self.move_disk(aux, destination , source, n -1 )
        else:
            print("Not Implemented Yet")

        self.print()

    def solve(self) -> None:
        for i in range(1, self._disks + 1):
            self._towers[0].push(i)

        self.print()

        self.move_disk(0, 2, 1, self._disks)        

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
    

if __name__ == "__main__":

    hanoiTowerSolver: HanoiTowerSolver = HanoiTowerSolver(3)

    hanoiTowerSolver.solve()

    print("---------")
    
