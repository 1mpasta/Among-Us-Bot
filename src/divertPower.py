from time import sleep

import cv2 as cv
import keyboard
import numpy as np
import win32api
import win32con
from PIL import ImageGrab

from task import Task
from utility import Utility


class DivertPower(Task):
    def __init__(self):
        self.slider = cv.imread(Utility.resource_path("media\\Divert_Power\\slider.png"), cv.IMREAD_COLOR)
        self.slider = Utility.resize_to_screen(self.slider, Utility.screenSize, (0.0432291666666667, 0.0601851851851852))

    def do_task(self):
        sleep(0.03)

        corner = (int(round(Utility.screenSize[0] * 0.3020833333333333)), int(round(Utility.screenSize[1] * 0.6972222222222222)))
        region = (
            corner[0], corner[1],
            corner[0] + int(round(Utility.screenSize[0] * 0.3958333333333333)),
            corner[1] + int(round(Utility.screenSize[1] * 0.062037037037037))
        )
        screenshot = ImageGrab.grab(region)
        screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

        click_point = Utility.get_location_from_image(self.slider, screenshot)
        click_point = (click_point[0] + corner[0], click_point[1] + corner[1])

        win32api.SetCursorPos(click_point)
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.02)
        win32api.SetCursorPos((click_point[0], Utility.screenSize[1] // 3))
        sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        sleep(0.01)
        keyboard.press_and_release("esc")

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.684375)), int(round(Utility.screenSize[1] * 0.4259259259259259))))
        if Utility.pixel_matches_color(pixel, (253, 255, 92)):
            return True
        return False
