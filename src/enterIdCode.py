from time import sleep

import cv2 as cv
import keyboard
import numpy as np
import win32api
from PIL import ImageGrab
from pytesseract import pytesseract

from task import Task
from utility import Utility


class EnterIdCode(Task):
    def __init__(self):
        self.cols = [
            int(round(Utility.screenSize[0] * 0.4375)),
            int(round(Utility.screenSize[0] * 0.5)),
            int(round(Utility.screenSize[0] * 0.5625)),
        ]
        self.rows = [
            int(round(Utility.screenSize[1] * 0.1296296296296296)),
            int(round(Utility.screenSize[1] * 0.2314814814814815)),
            int(round(Utility.screenSize[1] * 0.3240740740740741)),
            int(round(Utility.screenSize[1] * 0.4259259259259259)),
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
        gray = cv.cvtColor(np.array(image), cv.COLOR_RGB2GRAY)
        _, img_bw = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)

        mask = np.zeros((img_bw.shape[0] + 2, img_bw.shape[1] + 2), np.uint8)
        _, img_clean, _, _ = cv.floodFill(img_bw, mask, (0, 0), (255, 255, 255))

        contours, _ = cv.findContours(img_clean, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
        height = int(round(Utility.screenSize[1] * 0.0277777777777778))
        for i, cnt in enumerate(contours):
            if cv.boundingRect(cnt)[3] < height:
                img_clean = cv.drawContours(img_clean, contours, i, 255, -1)

        kernel = np.ones((2, 2))
        img_thin = cv.dilate(img_clean, kernel, iterations=1)

        top, bottom, left, right = [150] * 4
        img_border = cv.copyMakeBorder(img_thin, top, bottom, left, right, cv.BORDER_CONSTANT, value=(255, 255, 255))

        return img_border

    def do_task(self):
        x1 = int(round(Utility.screenSize[0] * 0.4114583333333333))
        y1 = int(round(Utility.screenSize[1] * 0.6638888888888889))
        x2 = int(round(Utility.screenSize[0] * 0.4791666666666667))
        y2 = int(round(Utility.screenSize[1] * 0.7037037037037037))

        win32api.SetCursorPos((int(round(Utility.screenSize[0] * 0.3958333333333333)), int(round(Utility.screenSize[1] * 0.8796296296296296))))
        sleep(0.01)
        Utility.click()

        screenshot = ImageGrab.grab()
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.3177083333333333)), int(round(Utility.screenSize[1] * 0.6111111111111111))))
        while Utility.pixel_matches_color(pixel, (84, 180, 114)):
            screenshot = ImageGrab.grab()
            pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.3177083333333333)), int(round(Utility.screenSize[1] * 0.6111111111111111))))

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
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.7786458333333333)), int(round(Utility.screenSize[1] * 0.7305555555555556))))
        pixel2 = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.7364583333333333)), int(round(Utility.screenSize[1] * 0.0657407407407407))))
        if Utility.pixel_matches_color(pixel, (40, 49, 35)) and Utility.pixel_matches_color(pixel2, (84, 180, 114)):
            return True
        return False
