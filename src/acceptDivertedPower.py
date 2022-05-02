from task import Task
from vision import Vision
from time import sleep
from PIL import Image
import keyboard
import win32api


class DivertPowerAccept(Task):

    def __init__(self, screenSize):
        self.vision = Vision()
        self.screenSize = screenSize

    def DoTask(self):
        win32api.SetCursorPos((self.screenSize[0] // 2, self.screenSize[1] // 2))
        sleep(0.01)
        Task.Click()
        sleep(1)
        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(self.screenSize[0] * 0.27604166666667)), int(round(self.screenSize[1] * 0.5185185185185185))))
        if self.vision.PixelMatchesColor(pixel, (127, 90, 0)):
            return True
        return False
