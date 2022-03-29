from time import sleep
from task import Task
import pyautogui
import win32api, win32con

class FuelEngines(Task):
    
    def DoTask(self):
        while pyautogui.pixelMatchesColor(1510, 745, (0, 90, 0)):
            win32api.SetCursorPos((1460, 880))
            sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
    def CheckTask(self):
        if pyautogui.pixelMatchesColor(1510, 745, (0, 90, 0)):
            return True
        return False
    