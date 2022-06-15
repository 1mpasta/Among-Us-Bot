from time import sleep

import win32api
from PIL import ImageGrab

from task import Task
from utility import Utility


class InspectSample(Task):

    def __init__(self):
        self.x = int(round(Utility.screenSize[0] * 0.3802083333333333))
        self.x_multiplier = int(round(Utility.screenSize[0] * 0.0598958333333333))
        self.sample_y = int(round(Utility.screenSize[1] * 0.5462962962962963))
        self.button_y = int(round(Utility.screenSize[1] * 0.7824074074074074))

    def do_task(self):
        screenshot = ImageGrab.grab()

        win32api.SetCursorPos((int(round(Utility.screenSize[0] * 0.6536458333333333)), int(round(Utility.screenSize[1] * 0.8657407407407407))))
        sleep(0.01)
        Utility.click()

        for i in range(6):
            pixel = screenshot.getpixel((self.x + self.x_multiplier * i, self.sample_y))
            if Utility.pixel_matches_color(pixel, (246, 134, 134)):
                win32api.SetCursorPos((self.x + self.x_multiplier * i, self.button_y))
                sleep(0.01)
                Utility.click()

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.5)), int(round(Utility.screenSize[1] * 0.1037037037037037))))
        pixel2 = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.6291666666666667)), int(round(Utility.screenSize[1] * 0.8444444444444444))))
        if Utility.pixel_matches_color(pixel, (0, 0, 0)) and Utility.pixel_matches_color(pixel2, (55, 53, 55)):
            return True
        return False
    