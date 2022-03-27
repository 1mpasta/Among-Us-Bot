from task import Task
from time import sleep
import keyboard
import pyautogui
import win32api

class DivertPowerAccept(Task):
    
    def DoTask(self):
        win32api.SetCursorPos((960, 550))
        sleep(0.01)
        Task.Click()
        sleep(0.03)
        keyboard.press_and_release("esc")

    def CheckTask(self):
        if pyautogui.pixelMatchesColor(530, 560, (127, 90, 0)):
            return True
        return False
    