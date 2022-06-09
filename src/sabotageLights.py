from time import sleep

import win32api
from PIL import ImageGrab

from task import Task
from utility import Utility


class SabotageLights(Task):
    def __init__(self):
        self.lights_y = int(round(Utility.screenSize[1] * 0.8333333333333333))
        self.switches_y = int(round(Utility.screenSize[1] * 0.7268518518518519))
        self.start_x = int(round(Utility.screenSize[0] * 0.3177083333333333))
        self.multiplier_x = int(round(Utility.screenSize[0] * 0.0911458333333333))

    def do_task(self, impostor_mode=False):
        screenshot = ImageGrab.grab()
        for i in range(5):
            pixel = screenshot.getpixel((self.start_x + int(round(self.multiplier_x * i)), self.lights_y))
            if Utility.pixel_matches_color(pixel, (0, 255, 0)) == impostor_mode:
                win32api.SetCursorPos((self.start_x + int(round(self.multiplier_x * i)), self.switches_y))
                sleep(0.01)
                Utility.click()
                sleep(0.01)
        sleep(0.15)

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.5208333333333333)), int(round(Utility.screenSize[1] * 0.0787037037037037))))
        if Utility.pixel_matches_color(pixel, (134, 89, 0)):
            return True
        return False
