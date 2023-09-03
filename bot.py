from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position: X:1100  Y:2840 RGB: ()
#Tile 2 Position: X:1318  Y:2840 RGB: ()
#Tile 3 Position: X:1515  Y:2840 RGB: ()
#Tile 4 Position: X:1724  Y:2840 RGB: ()

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(798, 2455)[0] == 17:
        click(798, 2455)
    if pyautogui.pixel(1007, 2455)[0] == 17:
        click(1007, 2455)
    if pyautogui.pixel(1211, 2455)[0] == 17:
        click(1211, 2455)
    if pyautogui.pixel(1391, 2455)[0] == 17:
        click(1391, 2455)
