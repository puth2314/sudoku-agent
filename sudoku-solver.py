def find_empty_cell(sudoku_board):
    for row in range(9):
        for col in range(9):
            if sudoku_board[row][col] == 0:
                return (row, col)
    return None
    

if __name__ == "__main__":
    pass