from time import sleep

import keyboard
import win32api

from task import Task
from utility import Utility


class DivertPowerAccept(Task):
    def do_task(self):
        win32api.SetCursorPos((Utility.screenSize[0] // 2, Utility.screenSize[1] // 2))
        sleep(0.01)
        Utility.click()
        sleep(0.5)
        keyboard.press_and_release("esc")

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.27604166666667)),int(round(Utility.screenSize[1] * 0.5185185185185185))))
        if Utility.pixel_matches_color(pixel, (127, 90, 0)):
            return True
        return False
