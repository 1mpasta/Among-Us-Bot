from time import sleep

import keyboard
import win32api

from task import Task
from utility import Utility


class StabilizeSteering(Task):
    def do_task(self):
        win32api.SetCursorPos((Utility.screenSize[0] // 2, Utility.screenSize[1] // 2))
        sleep(0.01)
        Utility.click()
        sleep(0.02)
        keyboard.press_and_release("esc")

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((Utility.screenSize[0] // 2, int(round(Utility.screenSize[1] * 0.1296296296296296))))
        pixel2 = screenshot.getpixel((Utility.screenSize[0] // 2, int(round(Utility.screenSize[1] * 0.8666666666666667))))
        if Utility.pixel_matches_color(pixel, (14, 63, 95)) and Utility.pixel_matches_color(pixel2, (14, 63, 95)):
            return True
        return False
