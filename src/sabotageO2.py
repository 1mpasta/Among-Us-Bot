from time import sleep

import cv2 as cv
import imutils
import keyboard
import numpy as np
import win32api
from PIL import ImageGrab
from pytesseract import pytesseract

from task import Task
from utility import Utility


class SabotageO2(Task):
    def __init__(self):
        self.cols = [
            int(round(Utility.screenSize[0] * 0.4140625)),
            int(round(Utility.screenSize[0] * 0.4973958333333333)),
            int(round(Utility.screenSize[0] * 0.5833333333333333)),
        ]
        self.rows = [
            int(round(Utility.screenSize[1] * 0.3518518518518519)),
            int(round(Utility.screenSize[1] * 0.5046296296296296)),
            int(round(Utility.screenSize[1] * 0.6574074074074074)),
            int(round(Utility.screenSize[1] * 0.8055555555555556)),
        ]
        self.button_positions = [
            (self.cols[1], self.rows[3]),
            (self.cols[0], self.rows[0]),
            (self.cols[1], self.rows[0]),
            (self.cols[2], self.rows[0]),
            (self.cols[0], self.rows[1]),
            (self.cols[1], self.rows[1]),
            (self.cols[2], self.rows[1]),
            (self.cols[0], self.rows[2]),
            (self.cols[1], self.rows[2]),
            (self.cols[2], self.rows[2]),
        ]

    def preprocess_for_ocr(self, image):
        # convert to black and white
        gray = cv.cvtColor(np.array(image), cv.COLOR_RGB2GRAY)
        _, img_bw = cv.threshold(gray, 165, 255, cv.THRESH_BINARY)
        # fix rotation
        inverted = cv.bitwise_not(img_bw)
        rotated = imutils.rotate(inverted, -25)
        inverted = cv.bitwise_not(rotated)
        # add border
        top, bottom, left, right = [150] * 4
        img_border = cv.copyMakeBorder(inverted, top, bottom, left, right, cv.BORDER_CONSTANT, value=(255, 255, 255))

        return img_border

    def do_task(self):
        x1 = int(round(Utility.screenSize[0] * 0.646875))
        y1 = int(round(Utility.screenSize[1] * 0.2722222222222222))
        x2 = int(round(Utility.screenSize[0] * 0.6958333333333333))
        y2 = int(round(Utility.screenSize[1] * 0.3287037037037037))

        screenshot = ImageGrab.grab((x1, y1, x2, y2))
        screenshot = self.preprocess_for_ocr(screenshot)
        code = pytesseract.image_to_string(screenshot)
        code = "".join(filter(str.isdigit, code))

        for number in code:
            win32api.SetCursorPos(self.button_positions[int(number)])
            sleep(0.02)
            Utility.click()
            sleep(0.01)

        button_enter = (self.cols[2], self.rows[3])
        win32api.SetCursorPos(button_enter)
        sleep(0.02)
        Utility.click()
        keyboard.press_and_release("esc")

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.7322916666666667)), int(round(Utility.screenSize[1] * 0.4009259259259259))))
        if Utility.pixel_matches_color(pixel, (181, 165, 68)):
            return True
        return False
