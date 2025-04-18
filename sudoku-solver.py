def find_empty_cell(sudoku_board):

    for row in range(9):
        for col in range(9):
            if sudoku_board[row][col] == 0:
                return (row, col)
            
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
    

if __name__ == "__main__":
    pass