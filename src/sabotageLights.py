from time import sleep
from task import Task
from vision import Vision
from PIL import ImageGrab
import win32api


class SabotageLights(Task):

    def __init__(self, screenSize):
        self.vision = Vision()
        self.screenSize = screenSize

        self.lightsY = int(round(screenSize[1] * 0.8333333333333333))
        self.switchesY = int(round(screenSize[1] * 0.7268518518518519))
        self.startX = int(round(screenSize[0] * 0.3177083333333333))
        self.multiplierX = int(round(screenSize[0] * 0.0911458333333333))

    def DoTask(self, impostorMode):
        screenshot = ImageGrab.grab()
        for i in range(5):
            pixel = screenshot.getpixel((self.startX + int(round(self.multiplierX * i)), self.lightsY))
            if self.vision.PixelMatchesColor(pixel, (0, 255, 0)) == impostorMode:
                win32api.SetCursorPos((self.startX + int(round(self.multiplierX * i)), self.switchesY))
                sleep(0.01)
                Task.Click()
                sleep(0.01)

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(self.screenSize[0] * 0.5208333333333333)), int(round(self.screenSize[1] * 0.0787037037037037))))
        if self.vision.PixelMatchesColor(pixel, (134, 89, 0)):
            return True
        return False
