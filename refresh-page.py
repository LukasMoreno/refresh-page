import pyautogui
import time

number_of_pages = 2
n = number_of_pages -1
count = 0

pyautogui.FAILSAFE = False
time.sleep(10)

while True:
    if count == n:
        pyautogui.hotkey ('ctrl','f5')
        count = 0
    else:
        time.sleep(10)
        pyautogui.hotkey ('ctrl','f5')
        count = count +1

    pyautogui.keyDown ('ctrl')
    pyautogui.press ('tab')
    pyautogui.keyUp ('ctrl')
    time.sleep(10)
