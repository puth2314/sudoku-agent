from copy import deepcopy

def find_empty_cell(sudoku_board):

    for row in range(9):
        for column in range(9):
            if sudoku_board[row][column] == 0:
                return (row, column)
            
    return None


def is_valid_guess(sudoku_board, row, column, guess):

    for x in range(9):
        if sudoku_board[row][x] == guess:
            return False
        
    for x in range(9):
        if sudoku_board[x][column] == guess:
            return False
        
    row_0 = (row // 3) * 3
    col_0 = (column // 3) * 3

    for box_row in range(row_0, row_0 + 3):
        for box_col in range(col_0, col_0 + 3):
            if sudoku_board[box_row][box_col] == guess:
                return False

    return True


def is_end_of_tree(sudoku_board):
    return find_empty_cell(sudoku_board)


def get_choices():
    """
    Will add more clever choices, like pruning, later.
    """
    return {1, 2, 3, 4, 5, 6, 7, 8, 9}


def backtrack_solve(sudoku_board, stop_at_first_solution:bool=True, max_solutions=2):
    solutions_list = list()

    def recursive_backtrack_solve(sudoku_board):
        """
        maybe implement using the coords to represent the child node?
        """
        # solution is when at end of tree, which is when no empty cells
        if find_empty_cell(sudoku_board) is None:
            solutions_list.append(deepcopy(sudoku_board))
            # either stop/continue the recursion when solution is found
            if stop_at_first_solution:
                return True
            if len(solutions_list) == max_solutions:
                return True
            return False
        
        row, col = find_empty_cell(sudoku_board)
            
        for choice in get_choices():
            if is_valid_guess(sudoku_board, row, col, choice):
                sudoku_board[row][col] = choice # go forward to parent node (aka depthfirstsearch)
                should_exit_resursion = recursive_backtrack_solve(sudoku_board)
                if should_exit_resursion:
                    return True # stop the recursion
                # (implicit) continue the recursion
                sudoku_board[row][col] = 0 # go backward to parent node (aka backtracking)
            # (implicit) continue the iteration

        # no more valid choices, exit this recursion nest
        return False # continue the recursion

    recursive_backtrack_solve(sudoku_board)

    return solutions_list


def print_solutions(solutions_list):
    if len(solutions_list) == 1:
        print("Found a unique solution: ")
        print(solutions_list)
    elif len(solutions_list) > 1:
        print(f"Found {len(solutions_list)} solutions: ")
        for i, solution in enumerate(solutions_list, start=1):
            print(f"Solution {i}: ")
            print(solution)
    else:
        print("No solution exists.")



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

    # backtrack_solve(sudoku_board, find_all_solutions=True, solutions_list=solutions_list)
    # print_solutions(solutions_list)
    solutions_list = backtrack_solve(sudoku_board, stop_at_first_solution=False)
    print(solutions_list)

