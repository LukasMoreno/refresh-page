# This script was created to switch browser tabs and refresh then. This can be used for monitoring pages for example.

import pyautogui
import time

# Insert here the number of tabs
number_of_tabs = 2
n = number_of_tabs -1
count = 0

pyautogui.FAILSAFE = False
time.sleep(10)

while True:
    if count == n:
        pyautogui.hotkey ('ctrl','f5')
        count = 0
    else:
# If you wont want the tabs refresh in different times, delete the next two lines
        time.sleep(10)
        pyautogui.hotkey ('ctrl','f5')
        count = count +1

    pyautogui.keyDown ('ctrl')
    pyautogui.press ('tab')
    pyautogui.keyUp ('ctrl')
    time.sleep(10)
