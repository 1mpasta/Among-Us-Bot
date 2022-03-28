from time import sleep
from task import Task
import keyboard
import pyautogui
import win32api
import cv2 as cv
import numpy as np

from vision import Vision

class UnlockManifolds(Task):

    vision = Vision()
    
    def DoTask(self):
        screenshot = pyautogui.screenshot(region=(575,385,765,305))
        for i in range(1, 11, 1):
            number = cv.imread("media/Unlock_Manifolds/"+str(i)+".png", cv.IMREAD_COLOR)
        
            screenshot = np.array(screenshot)
            screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
            
            clickPoint = self.vision.GetLocationFromPicture(number, screenshot)
            clickPoint = (clickPoint[0]+575,clickPoint[1]+385)
        
            win32api.SetCursorPos(clickPoint)
            sleep(0.01)
            Task.Click()
        keyboard.press_and_release("esc")
    
    def CheckTask(self):
        if pyautogui.pixelMatchesColor(1279, 385, (0, 64, 222)):
            return True
        return False
