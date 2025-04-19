from copy import deepcopy
import numpy as np
from dataclasses import dataclass


BOX_LENGTH = 3
BOARD_LENGTH = 9
BOARD_HEIGHT = 9
BOARD_WIDTH = 9


@dataclass
class Choice:

    num: int = None
    row: int = None
    col: int = None

    def __post_init__(self):

        if self.num is not None:
            if not (1 <= self.num <= 9):
                raise ValueError("Choice number must be between 1 and 9, not {}.".format(self.num))
        
        if self.row is not None:
            if not (0 <= self.row <= 8):
                raise ValueError("Choice row must be between 0 and 8, not {}.".format(self.row))
        
        if self.col is not None: 
            if not (0 <= self.col <= 8):
                raise ValueError("Choice column must be between 0 and 8, not {}.".format(self.col))


def find_empty_cell(sudoku_board):

    for row in range(9):
        for column in range(9):
            if sudoku_board[row][column] == 0:
                return (row, column)
            
    return None


def is_valid_guess(sudoku_board, 
                   choice: Choice):
    
    row = choice.row
    col = choice.col
    guess = choice.num

    for x in range(9):
        if sudoku_board[row][x] == guess:
            return False
        
    for x in range(9):
        if sudoku_board[x][col] == guess:
            return False
        
    row_0 = (row // 3) * 3
    col_0 = (col // 3) * 3

    for box_row in range(row_0, row_0 + 3):
        for box_col in range(col_0, col_0 + 3):
            if sudoku_board[box_row][box_col] == guess:
                return False

    return True


def get_candidates(candidate_board, row, col):
    """
    will add more clever choices, like pruning, later...
    """
    return candidate_board[row, col]


def backtrack_solve(sudoku_board,
                    nth_solution_stop: int = 1):
    
    solutions_list = list()

    candidates_board = np.zeros(shape=(BOARD_HEIGHT, BOARD_WIDTH), dtype=list)
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            # filled_number = int(board_string[i*BOARD_HEIGHT + j])
            filled_number = sudoku_board[i][j]
            if filled_number:
                candidates_board[i, j] = [filled_number]
            else:
                candidates_board[i, j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def recursive_backtrack_solve(sudoku_board):
        """
        maybe implement using the coords to represent the child node?
        """
        # solution is when at end of tree, which is when no more empty cells
        empty_cell = find_empty_cell(sudoku_board)
        if empty_cell is None:
            solutions_list.append(deepcopy(sudoku_board))
            # stop the recursion when the nth solution, otherwise exit just this recursion nest
            return len(solutions_list) == nth_solution_stop
        
        my_choice = Choice()
        my_choice.row, my_choice.col = empty_cell
        for my_choice.num in get_candidates(candidates_board, my_choice.row, my_choice.col):
            if is_valid_guess(sudoku_board, my_choice):
                sudoku_board[my_choice.row][my_choice.col] = my_choice.num # go forward to parent node (aka depthfirstsearch)
                should_exit_resursion = recursive_backtrack_solve(sudoku_board)
                if should_exit_resursion:
                    return True # stop the recursion
                # (implicit) continue the recursion
                sudoku_board[my_choice.row][my_choice.col] = 0 # go backward to parent node (aka backtracking)
            # (implicit) continue the iteration

        # no more valid choices, exit just this recursion nest
        return False # continue the recursion

    recursive_backtrack_solve(sudoku_board)

    return solutions_list


def print_solutions(solutions_list):

    if len(solutions_list) == 0:
        print("Found no solution.")
        return
    
    for index, solution in enumerate(solutions_list, start=1):
        print("Solution {}:".format(index))
        print(solution)
        
        
if __name__ == "__main__":

    # sudoku_board = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    # ]

    sudoku_board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solutions_list = backtrack_solve(sudoku_board, nth_solution_stop=2)
    print_solutions(solutions_list)
