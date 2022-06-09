from time import sleep

import win32api

from task import Task
from utility import Utility


class Download(Task):
    def do_task(self):
        win32api.SetCursorPos((Utility.screenSize[0] // 2, int(round(Utility.screenSize[1] * 0.6111111111111111))))
        sleep(0.01)
        Utility.click()
        sleep(0.5)

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.7536458333333333)), int(round(Utility.screenSize[1] * 0.2055555555555556))))
        if Utility.pixel_matches_color(pixel, (78, 112, 148)):
            return True
        return False
