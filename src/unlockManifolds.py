from time import sleep
from task import Task
import keyboard
import pyautogui
import win32api
import cv2 as cv
import numpy as np


class UnlockManifolds(Task):

    def __init__(self):
        self.numbers = []
        for i in range(1, 11, 1):
            number = cv.imread(f"media/Unlock_Manifolds/{str(i)}.png", cv.IMREAD_COLOR)
            number = Task.vision.ResizeToScreen(number, Task.screenSize, (0.0770833333333333, 0.137037037037037))
            self.numbers.append(number)

    def DoTask(self):
        x1 = int(round(Task.screenSize[0] * 0.3020833333333333))
        y1 = int(round(Task.screenSize[1] * 0.3601851851851852))
        x2 = int(round(Task.screenSize[0] * 0.6979166666666667))
        y2 = int(round(Task.screenSize[1] * 0.6398148148148148))

        screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
        screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
        for number in self.numbers:
            clickPoint = Task.vision.GetLocationFromPicture(number, screenshot)
            clickPoint = (clickPoint[0] + x1, clickPoint[1] + y1)
            win32api.SetCursorPos(clickPoint)
            sleep(0.01)
            Task.Click()
        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(Task.screenSize[0] * 0.6661458333333333)), int(round(Task.screenSize[1] * 0.3564814814814815))))
        if Task.vision.PixelMatchesColor(pixel, (0, 64, 222)):
            return True
        return False
