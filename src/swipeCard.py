from time import sleep

import keyboard
import win32api
import win32con
from PIL import ImageGrab

from task import Task
from utility import Utility


class SwipeCard(Task):
    def __init__(self):
        self.swipe_time = 0.05
        self.segments = 25
        self.start_x = int(round(Utility.screenSize[0] * 0.2890625))
        self.end_x = int(round(Utility.screenSize[0] * 0.7552083333333333))
        self.y = int(round(Utility.screenSize[1] * 0.3796296296296296))

    def do_task(self):
        win32api.SetCursorPos((int(round(Utility.screenSize[0] * 0.390625)), int(round(Utility.screenSize[1] * 0.7962962962962963))))
        sleep(0.01)
        Utility.click()

        pixel_pos = (int(round(Utility.screenSize[0] * 0.7005208333333333)), int(round(Utility.screenSize[1] * 0.3009259259259259)))
        screenshot = ImageGrab.grab()
        pixel = screenshot.getpixel(pixel_pos)
        while Utility.pixel_matches_color(pixel, (0, 99, 71)):
            screenshot = ImageGrab.grab()
            pixel = screenshot.getpixel(pixel_pos)

        win32api.SetCursorPos((self.start_x, self.y))
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.02)
        for i in range(1, self.segments + 1):
            next_pos = self.start_x + int(((self.end_x - self.start_x) // self.segments) * i)
            win32api.SetCursorPos((next_pos, self.y))
            sleep(self.swipe_time / self.segments)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        keyboard.press_and_release("esc")

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.690625)), int(round(Utility.screenSize[1] * 0.1166666666666667))))
        pixel2 = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.6770833333333333)), int(round(Utility.screenSize[1] * 0.8611111111111111))))
        if Utility.pixel_matches_color(pixel, (22, 74, 57)) and Utility.pixel_matches_color(pixel2, (71, 147, 52)):
            return True
        return False
