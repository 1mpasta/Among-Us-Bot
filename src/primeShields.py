from task import Task
from vision import Vision
from time import sleep
from PIL import ImageGrab
import cv2 as cv
import numpy as np
import keyboard
import win32api


class PrimeShields(Task):

    def __init__(self, screenSize):
        self.vision = Vision()
        self.screenSize = screenSize

        self.positions = [
            (int(round(screenSize[0] * 0.4895833333333333)), int(round(screenSize[1] * 0.3148148148148148))),
            (int(round(screenSize[0] * 0.5963541666666667)), int(round(screenSize[1] * 0.3703703703703704))),
            (int(round(screenSize[0] * 0.6171875)), int(round(screenSize[1] * 0.6481481481481481))),
            (int(round(screenSize[0] * 0.4895833333333333)), int(round(screenSize[1] * 0.7314814814814815))),
            (int(round(screenSize[0] * 0.3697916666666667)), int(round(screenSize[1] * 0.6111111111111111))),
            (int(round(screenSize[0] * 0.359375)), int(round(screenSize[1] * 0.3981481481481481))),
            (int(round(screenSize[0] * 0.4921875)), int(round(screenSize[1] * 0.5231481481481481)))
        ]
        self.colorsSkeld = [
            140,
            140,
            140,
            100,
            140,
            100,
            140
        ]
        self.colorsMira = [
            (174, 62, 92),
            (190, 75, 98),
            (190, 75, 98),
            (174, 62, 92),
            (190, 75, 98),
            (202, 84, 104),
            (174, 62, 92)
        ]

    def DoTask(self):
        screenshot = ImageGrab.grab()
        screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2GRAY)

        for i, pos in enumerate(self.positions):
            pixel = screenshot[pos[1], pos[0]]
            print(f"{i}: {pixel}")
            if pixel < self.colorsSkeld[i]:
                win32api.SetCursorPos(pos)
                sleep(0.01)
                Task.Click()
        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((self.screenSize[0] // 2, int(round(self.screenSize[1] * 0.0787037037037037))))
        if self.vision.PixelMatchesColor(pixel, (13, 29, 60)):
            return True
        return False
