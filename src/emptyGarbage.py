from time import sleep

import keyboard
import win32api
import win32con

from task import Task
from utility import Utility


class EmptyGarbage(Task):
    def do_task(self):
        win32api.SetCursorPos((int(round(Utility.screenSize[0] * 0.6614583333333333)), int(round(Utility.screenSize[1] * 0.3888888888888889))))
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.02)
        win32api.SetCursorPos((int(round(Utility.screenSize[0] * 0.6614583333333333)), int(round(Utility.screenSize[1] * 0.8333333333333333))))
        sleep(1.35)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        sleep(0.03)
        keyboard.press_and_release("esc")

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.625)), int(round(Utility.screenSize[1] * 0.4675925925925926))))
        if Utility.pixel_matches_color(pixel, (145, 175, 187)):
            return True
        return False
