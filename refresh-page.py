# This script was created to switch browser tabs and refresh then. This can be used for monitoring pages for example.

import pyautogui
import time

# Insert here the number of tabs
number_of_tabs = 2
count = 1

pyautogui.FAILSAFE = False
time.sleep(10)

while True:
    if count == number_of_tabs:
        pyautogui.hotkey ('ctrl','f5')
        count = 1
    else:
# If you wont want the tabs refresh in different times, delete the next two lines
        time.sleep(10)
        pyautogui.hotkey ('ctrl','f5')
        count = count +1

    pyautogui.keyDown ('ctrl')
    pyautogui.press ('tab')
    pyautogui.keyUp ('ctrl')
    time.sleep(10)
