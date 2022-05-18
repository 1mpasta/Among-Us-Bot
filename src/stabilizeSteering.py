from time import sleep
from task import Task
from vision import Vision
import keyboard
import win32api


class StabilizeSteering(Task):

    def __init__(self, screenSize):
        self.vision = Vision()
        self.screenSize = screenSize

    def DoTask(self):
        win32api.SetCursorPos((self.screenSize[0] // 2, self.screenSize[1] // 2))
        sleep(0.01)
        Task.Click()
        sleep(0.02)
        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((self.screenSize[0] // 2, int(round(self.screenSize[1] * 0.1296296296296296))))
        pixel2 = screenshot.getpixel((self.screenSize[0] // 2, int(round(self.screenSize[1] * 0.8666666666666667))))
        if self.vision.PixelMatchesColor(pixel, (14, 63, 95)) and self.vision.PixelMatchesColor(pixel2, (14, 63, 95)):
            return True
        return False
