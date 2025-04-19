import keyboard
import pyautogui
import time

def calibrate_grid_size():
    
    print("")
    print("INSTRUCTIONS FOR CALIBRATION:")
    print("1. Move mouse to the TOP-LEFT-MOST cell and press 's'.")
    print("2. Move mouse to the CENTER cell of the TOP-LEFT 3x3 box and press 's'.")
    print("3. Move mouse to the BOTTOM-RIGHT-MOST cell and press 's'.")
    print("")

    while not keyboard.is_pressed('s'):
        continue

    x1, y1 = pyautogui.position()
    print(f"Recorded top-left-most cell: ({x1}, {y1}) px")

    time.sleep(1)

    while not keyboard.is_pressed('s'):
        continue
    
    x2, y2 = pyautogui.position()
    print(f"Recorded center cell of top-left box: ({x2}, {y2}) px")

    time.sleep(1)

    while not keyboard.is_pressed('s'):
        continue

    x3, y3 = pyautogui.position()
    print(f"Recorded bottom-right-most cell: ({x3}, {y3}) px")


    cell_size = int((abs(x2 - x1) + abs(y2 - y1)) / 2)
    # abs(y3 - y1) = box_gap_y * 2 + cell_size * 8
    # => box_gap_y = (abs(y3 - y1) - cell_size * 8) / 2
    box_gap = int((abs(x3 - x1) + abs(y3 - y1) - cell_size * 16) / 4)
    print("")
    print(f"Estimated cell size: {cell_size} px")
    print(f"Estimated box gap: {box_gap} px")
    
    # assert x2-x1>7
    # assert box gap is not negative

def main():
    calibrate_grid_size()


if __name__ == "__main__":
    main()