from time import sleep
from task import Task
import pyautogui
import win32api

class Download(Task):

    def DoTask(self):
        win32api.SetCursorPos((960, 660))
        sleep(0.01)
        Task.Click()
        sleep(0.5)
    
    def CheckTask(self):
        if pyautogui.pixelMatchesColor(1447, 222, (78, 112, 148)):
            return True
        return False
    