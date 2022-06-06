from time import sleep
from task import Task
from PIL import ImageGrab
import win32api
import win32con


class FuelEngines(Task):

    def __init__(self):
        self.checkPixelCoords = (int(round(Task.screenSize[0] * 0.7864583333333333)), int(round(Task.screenSize[1] * 0.6898148148148148)))

    def DoTask(self):
        screenshot = ImageGrab.grab()
        pixel = screenshot.getpixel(self.checkPixelCoords)
        while Task.vision.PixelMatchesColor(pixel, (0, 90, 0)):
            win32api.SetCursorPos((int(round(Task.screenSize[0] * 0.7604166666666667)), int(round(Task.screenSize[1] * 0.8148148148148148))))
            sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            pixel = ImageGrab.grab().getpixel(self.checkPixelCoords)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel(self.checkPixelCoords)
        if Task.vision.PixelMatchesColor(pixel, (0, 90, 0)):
            return True
        return False
