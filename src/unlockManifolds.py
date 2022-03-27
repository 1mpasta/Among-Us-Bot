from time import sleep
from task import Task
import keyboard
import pyautogui
import win32api
import cv2 as cv
import numpy as np

class UnlockManifolds(Task):

    # detection area x1 575 y1 385 x2 1340 y2 690 w765 h305
    
    def DoTask(self):
        screenshot = pyautogui.screenshot(region=(575,385,765,305))
        for i in range(1, 11, 1):
            number = cv.imread("media/Unlock_Manifolds/"+str(i)+".png", cv.IMREAD_COLOR)
        
            screenshot = np.array(screenshot)
            screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        
            result = cv.matchTemplate(screenshot, number, cv.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

            clickPoint = (max_loc[0] + 26 + 575, max_loc[1] + 35 + 385)
        
            win32api.SetCursorPos(clickPoint)
            sleep(0.01)
            Task.Click()
        keyboard.press_and_release("esc")
    
    def CheckTask(self):
        if pyautogui.pixelMatchesColor(1279, 385, (0, 64, 222)):
            return True
        return False
