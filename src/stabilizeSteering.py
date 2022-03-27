from time import sleep
from task import Task
import keyboard
import pyautogui
import win32api

class StabilizeSteering(Task):

    def DoTask(self):
        win32api.SetCursorPos((960, 540))
        sleep(0.01)
        Task.Click()
        sleep(0.02)
        keyboard.press_and_release("esc")

    def CheckTask(self):
        if pyautogui.pixelMatchesColor(960, 140, (14, 63, 95)):
            return True
        return False
