import pyautogui
import cv2
import numpy as np
import time 
import keyboard


def fill_board_from_screenshot(start_x, start_y, cell_size, box_gap):
    screenshot_file = 'images/screenshot.png'

    time.sleep(1)

    while not keyboard.is_pressed('s'):
        continue

    img = np.array(pyautogui.screenshot())
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # img = cv2.imread(screenshot_file, cv2.IMREAD_GRAYSCALE)
    # height, width = img.shape
    # img = img[0:height, (width//2)-(height//2):(width//2)+(height//2)]

    iteration = 0
    board = [[0 for col in range(9)] for row in range(9)]
    for row in range(9):
        for col in range(9):
            x1 = start_x + (cell_size * col) + (box_gap * (col // 3)) - (cell_size // 2)
            x2 = x1 + cell_size
            y1 = start_y + (cell_size * row) + (box_gap * (row // 3)) - (cell_size // 2)
            y2 = y1 + cell_size
            img_crop = img[y1:y2, x1:x2]
            img_crop = cv2.GaussianBlur(img_crop, (5,5), 0)
            img_crop = cv2.Canny(img_crop, 50, 150)

            for i in range(1, 10):
                iteration += 1
                # if iteration % 50 == 0:
                #     print(f"iteration {iteration} row {row} col {col} num {i}")
                template = cv2.imread(f'images/numbers_raw/number_{i}.png', cv2.IMREAD_GRAYSCALE)
                template = cv2.GaussianBlur(template, (5,5), 0)
                template = cv2.Canny(template, 50, 150)
                result = cv2.matchTemplate(img_crop, template, cv2.TM_CCOEFF_NORMED)

                threshold = 0.9
                if np.any(result > threshold):
                    board[row][col] = i
                    break

    return board
            

def main():
    pass
            

if __name__ == "__main__":
    print("Reading board...")
    main()
