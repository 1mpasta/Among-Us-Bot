from task import Task
from time import sleep
from PIL import ImageGrab
import keyboard
import win32api


class CalibrateDistributor(Task):

    def __init__(self):
        self.x = int(round(Task.screenSize[0] * 0.6380208333333333))
        self.screenY = int(round(Task.screenSize[1] * 0.212962962962963))
        self.buttonY = int(round(Task.screenSize[1] * 0.2962962962962963))
        self.screenMultiplier = int(round(Task.screenSize[1] * 0.25))
        self.buttonMultiplier = int(round(Task.screenSize[1] * 0.2407407407407407))

    def DoTask(self):
        screenshot = ImageGrab.grab()

        pixel = screenshot.getpixel((self.x, self.screenY))
        while Task.vision.PixelMatchesColor(pixel, (0, 0, 0)):
            screenshot = ImageGrab.grab()
            pixel = screenshot.getpixel((self.x, self.screenY))

        win32api.SetCursorPos((self.x, self.buttonY))
        sleep(0.01)
        Task.Click()

        pixel = screenshot.getpixel((self.x, self.screenY + self.screenMultiplier))
        while Task.vision.PixelMatchesColor(pixel, (0, 0, 0)):
            screenshot = ImageGrab.grab()
            pixel = screenshot.getpixel((self.x, self.screenY + self.screenMultiplier))

        win32api.SetCursorPos((self.x, self.buttonY + self.buttonMultiplier))
        sleep(0.01)
        Task.Click()

        pixel = screenshot.getpixel((self.x, self.screenY + (self.screenMultiplier * 2)))
        while Task.vision.PixelMatchesColor(pixel, (0, 0, 0)):
            screenshot = ImageGrab.grab()
            pixel = screenshot.getpixel((self.x, self.screenY + (self.screenMultiplier * 2)))

        win32api.SetCursorPos((self.x, self.buttonY + (self.buttonMultiplier * 2)))
        sleep(0.01)
        Task.Click()
        sleep(0.01)
        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(Task.screenSize[0] * 0.5828125)), int(round(Task.screenSize[1] * 0.1962962962962963))))
        if Task.vision.PixelMatchesColor(pixel, (255, 227, 0)):
            return True
        return False
