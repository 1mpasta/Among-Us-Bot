from time import sleep

import win32api
import win32con
from PIL import ImageGrab

from task import Task
from utility import Utility


class FuelEngines(Task):
    def __init__(self):
        self.check_pixel_coords = (int(round(Utility.screenSize[0] * 0.7864583333333333)), int(round(Utility.screenSize[1] * 0.6898148148148148)))

    def do_task(self):
        screenshot = ImageGrab.grab()
        pixel = screenshot.getpixel(self.check_pixel_coords)
        while Utility.pixel_matches_color(pixel, (0, 90, 0)):
            win32api.SetCursorPos((int(round(Utility.screenSize[0] * 0.7604166666666667)), int(round(Utility.screenSize[1] * 0.8148148148148148))))
            sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            pixel = ImageGrab.grab().getpixel(self.check_pixel_coords)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def check_task(self, screenshot):
        pixel = screenshot.getpixel(self.check_pixel_coords)
        if Utility.pixel_matches_color(pixel, (0, 90, 0)):
            return True
        return False
