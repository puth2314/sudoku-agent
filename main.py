import keyboard
import pyautogui
import time

import sudoku_writer
import sudoku_reader
import sudoku_solver


def calibrate_grid_size():
    
    print("")
    print("INSTRUCTIONS FOR CALIBRATION:")
    print("1. Move mouse to the TOP-LEFT-MOST cell and press 's'.")
    print("2. Move mouse to the CENTER cell of the TOP-LEFT 3x3 box and press 's'.")
    print("3. Move mouse to the BOTTOM-RIGHT-MOST cell and press 's'.")
    print("")

    def record_mouse_position(key_to_press: str = 's'):
        while not keyboard.is_pressed(key_to_press):
            continue
        return pyautogui.position()

    x1, y1 = record_mouse_position(key_to_press='s')
    print(f"Recorded top-left-most cell: ({x1}, {y1}) px")

    time.sleep(1)
    
    x2, y2 = record_mouse_position(key_to_press='s')
    print(f"Recorded center cell of top-left box: ({x2}, {y2}) px")

    time.sleep(1)

    x3, y3 = record_mouse_position(key_to_press='s')
    print(f"Recorded bottom-right-most cell: ({x3}, {y3}) px")

    def calculate_cell_size(x1, y1, x2, y2):
        # assert x2 - x1 > 7
        cell_size_x = x2 - x1 # abs(x2 - x1)
        cell_size_y = y2 - y1 # abs(y2 - y1)
        cell_size_avg = (cell_size_x - cell_size_y) / 2
        return int(cell_size_avg)
    
    cell_size = calculate_cell_size(x1, y1, x2, y2)

    def calculate_box_gap(x1, y1, x3, y3, cell_size):
        # assert x3 - x1 > 7 * 8 = 56
        # start derivation
        # abs(y3 - y1) = box_gap_y * 2 + cell_size * 8
        # => box_gap_y = (abs(y3 - y1) - cell_size * 8) / 2
        # end derivation
        box_gap_x = x3 - x1
        box_gap_y = y3 - y1
        box_gap_avg = (box_gap_x + box_gap_y - (cell_size * 16)) / 4
        return int(box_gap_avg)
    
    box_gap = calculate_box_gap(x1, y1, x3, y3, cell_size)

    print("")
    print(f"Estimated cell size: {cell_size} px")
    print(f"Estimated box gap: {box_gap} px")

    return x1, y1, cell_size, box_gap


def main():
    x_topleft, y_topleft, cell_size, box_gap = calibrate_grid_size()

    board = sudoku_reader.fill_board_from_screenshot(x_topleft, y_topleft, cell_size, box_gap)
    solution = sudoku_solver.backtrack_solve(board)
    sudoku_writer.move_through_board(x_topleft, y_topleft, cell_size, box_gap, solution[0])


if __name__ == "__main__":
    main()