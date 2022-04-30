from time import sleep
from task import Task
from vision import Vision
import win32api

class Download(Task):

    def __init__(self, screenSize):
        self.vision = Vision()
        self.screenSize = screenSize

    def DoTask(self):
        win32api.SetCursorPos((self.screenSize[0] // 2, int(round(self.screenSize[1] * 0.6111111111111111))))
        sleep(0.01)
        Task.Click()
        sleep(0.5)
    
    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(self.screenSize[0] * 0.7536458333333333)), int(round(self.screenSize[1] * 0.2055555555555556))))
        if self.vision.PixelMatchesColor(pixel, (78, 112, 148)):
            return True
        return False
    