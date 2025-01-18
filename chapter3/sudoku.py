
from typing import List


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