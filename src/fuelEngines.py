from time import sleep
from task import Task
from vision import Vision
from PIL import ImageGrab
import win32api, win32con

class FuelEngines(Task):
    
    def __init__(self, screenSize):
        self.vision = Vision()
        self.screenSize = screenSize
        self.checkPixelCoords = (int(round(screenSize[0] * 0.7864583333333333)), int(round(screenSize[1] * 0.6898148148148148)))
    
    def DoTask(self):
        screenshot = ImageGrab.grab()
        pixel = screenshot.getpixel(self.checkPixelCoords)
        while self.vision.PixelMatchesColor(pixel, (0, 90, 0)):
            win32api.SetCursorPos((int(round(self.screenSize[0] * 0.7604166666666667)), int(round(self.screenSize[1] * 0.8148148148148148))))
            sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            pixel = ImageGrab.grab().getpixel(self.checkPixelCoords)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel(self.checkPixelCoords)
        if self.vision.PixelMatchesColor(pixel, (0, 90, 0)):
            return True
        return False
    