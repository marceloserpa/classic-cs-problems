from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt

#from generic_search import dfs, bfs, node_to_path, astar, Node
from generic_search import dfs, node_to_path, Node

class Cell(str, Enum):
    EMPTY = "-"
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    row: int
    column: int

class Maze:

    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2,  start: MazeLocation = MazeLocation(0,0), goal: MazeLocation =  MazeLocation(9,9)) -> None:
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal

        # fill all cell vith empty value
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]

        self._randomly_fill(rows, columns, sparseness)

        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows: int, columns: int, sparseness: float) :

        print(self._grid[0][0])

        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED
                   

    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([column.value for column in row]) + "\n"
        return output

    def goal_test(self, location: MazeLocation) -> bool:
        return location == self.goal

    def successors(self, location: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if(location.row + 1 < self._rows and self._grid[location.row + 1][location.column] != Cell.BLOCKED):
            locations.append(MazeLocation(location.row + 1, location.column))
            
        if(location.row - 1 >= 0 and self._grid[location.row - 1][location.column] != Cell.BLOCKED):
            locations.append(MazeLocation(location.row - 1, location.column))

        if(location.column + 1 < self._columns and self._grid[location.row][location.column + 1] != Cell.BLOCKED):
            locations.append(MazeLocation(location.row, location.column + 1))

        if(location.column - 1 >= 0 and self._grid[location.row][location.column - 1] != Cell.BLOCKED):
            locations.append(MazeLocation(location.row, location.column - 1))

        return locations

    def mark(self, path: List[MazeLocation]) -> None:
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
        
    def clear(self, path: List[MazeLocation]) -> None:
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL



if __name__ == "__main__":

    print("Maze")
    maze: Maze = Maze()
    print(maze)
    solution1 :Optional[Node[MazeLocation]] = dfs(maze.start, maze.goal_test, maze.successors)

    if solution1 is None:
        print("No solution found using DFS")

    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)