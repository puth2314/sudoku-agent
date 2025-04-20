import keyboard
import pyautogui
import time

def move_through_board(start_x, start_y, cell_size, box_gap, solution):

    for row in range(9):
        for col in range(9):
            x = start_x + (cell_size * col) + (box_gap * (col // 3))
            y = start_y + (cell_size * row) + (box_gap * (row // 3))
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.press(str(solution[row][col]))
