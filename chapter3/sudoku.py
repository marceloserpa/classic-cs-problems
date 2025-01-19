
from typing import Dict, List, NamedTuple, Optional
from venv import create
from csp import Constraint, CSP



class SudokuConstraint(Constraint[str, int]):

    def __init__(self, squares: List[str]) -> None:
        super().__init__(squares)
        self.squares = squares

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        # Check that all values in assignment are unique
        assigned_values = [assignment[square] for square in self.squares if square in assignment]
        return len(assigned_values) == len(set(assigned_values))


def print_board(board: List[List[int]]) -> None:
    board_text: str = ""

    for row in range(9):

        if row == 3 or row == 6:
            board_text += f"________________________\n"

        for column in range(9):
            board_text += f"{board[row][column]} "
            if column == 8:
                board_text += "\n"

            if column == 2 or column == 5:
                board_text += " | "
            
    print(board_text)

def create_csp(board: List[List[int]]) -> CSP[List[str], Dict[str, List[int]]] :

    # initialize CSP

    # squares from board
    variables: List[str] = [] 

    # squares with pre-defined values or a list of possible values
    domains: Dict[str, List[int]] = {}

    size = len(board)

    for row in range(size):
        for col in range(size):

            square: str = f"{row}-{col}"
            variables.append(square)

            if board[row][col] == 0:
                domains[square] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                domains[square] = [board[row][col]]

    csp: CSP[List[str], Dict[str, List[int]] ] = CSP(variables, domains)

    # Setup constraints

    for row in range(size):
        
        # for rows
        row_squares = [f"{row}-{col}" for col in range(size)]
        csp.add_constraint(SudokuConstraint(row_squares))

        # for columns (inversing row and col)
        col_squares = [f"{col}-{row}" for col in range(size)]
        csp.add_constraint(SudokuConstraint(col_squares))

        # for sub-grid 3x3
        for box_row in range(3):
            for box_col in range(3):
                subgrid_squares = [
                    f"{row}-{col}"
                    for row in range(box_row * 3, box_row * 3 + 3)
                    for col in range(box_col * 3, box_col * 3 + 3)
                ]
                csp.add_constraint(SudokuConstraint(subgrid_squares))

    return csp  



if __name__ == "__main__":

    board: List[List[int]] = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]

    print_board(board)

    print("=====> ")

    csp: CSP[List[str], Dict[str, List[int]]] = create_csp(board)
    solution: Optional[Dict[str, List[int]]] = csp.backtracking_search()


    # Print the solution
    solution_board: List[List[int]] = []
    if solution:
        for row in range(9):
            solution_board.append([])
            for col in range(9):
               solution_board[row].append(solution[f"{row}-{col}"]) 

        print_board(solution_board)
    else:
        print("No solution found.")