from time import sleep

import cv2 as cv
import keyboard
import numpy as np
import win32api
from PIL import ImageGrab

from task import Task
from utility import Utility


class UnlockManifolds(Task):
    def __init__(self):
        self.numbers = []
        for i in range(1, 11, 1):
            number = cv.imread(Utility.resource_path(f"media\\Unlock_Manifolds\\{str(i)}.png"), cv.IMREAD_COLOR)
            number = Utility.resize_to_screen(number, Utility.screenSize, (0.0770833333333333, 0.137037037037037))
            self.numbers.append(number)

    def do_task(self):
        x1 = int(round(Utility.screenSize[0] * 0.3020833333333333))
        y1 = int(round(Utility.screenSize[1] * 0.3601851851851852))
        x2 = int(round(Utility.screenSize[0] * 0.6979166666666667))
        y2 = int(round(Utility.screenSize[1] * 0.6388888888888889))

        screenshot = ImageGrab.grab((x1, y1, x2, y2))
        screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
        for number in self.numbers:
            click_point = Utility.get_location_from_image(number, screenshot)
            click_point = (click_point[0] + x1, click_point[1] + y1)
            win32api.SetCursorPos(click_point)
            sleep(0.01)
            Utility.click()
        keyboard.press_and_release("esc")

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.6661458333333333)), int(round(Utility.screenSize[1] * 0.3564814814814815))))
        if Utility.pixel_matches_color(pixel, (0, 64, 222)):
            return True
        return False
