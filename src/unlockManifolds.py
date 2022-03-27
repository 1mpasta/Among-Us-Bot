from time import sleep
from task import Task
import keyboard
import pyautogui
import win32api

class UnlockManifolds(Task):

    # detection area x1 575 y1 385 x2 1340 y2 690 w765 h305
    
    def DoTask(self):
        for i in range(1, 11, 1):
            number = pyautogui.locateCenterOnScreen("media/Unlock_Manifolds/"+str(i)+".png", grayscale=True, confidence=0.62, region=(575, 385, 765, 305))
            win32api.SetCursorPos(number)
            sleep(0.01)
            Task.Click()
        keyboard.press_and_release("esc")

    def CheckTask(self):
        if pyautogui.pixelMatchesColor(1279, 385, (0, 64, 222)):
            return True
        return False
