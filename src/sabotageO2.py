from time import sleep
from task import Task
import cv2 as cv
import numpy as np
from vision import Vision
from PIL import ImageGrab
from pytesseract import pytesseract
import imutils
import keyboard
import win32api


class SabotageO2(Task):

    def __init__(self, screenSize):
        self.vision = Vision()
        self.screenSize = screenSize

        self.cols = [
            int(round(self.screenSize[0] * 0.4140625)),
            int(round(self.screenSize[0] * 0.4973958333333333)),
            int(round(self.screenSize[0] * 0.5833333333333333))
        ]
        self.rows = [
            int(round(self.screenSize[1] * 0.3518518518518519)),
            int(round(self.screenSize[1] * 0.5046296296296296)),
            int(round(self.screenSize[1] * 0.6574074074074074)),
            int(round(self.screenSize[1] * 0.8055555555555556))
        ]
        self.buttonPositions = [
            (self.cols[1], self.rows[3]),
            (self.cols[0], self.rows[0]),
            (self.cols[1], self.rows[0]),
            (self.cols[2], self.rows[0]),
            (self.cols[0], self.rows[1]),
            (self.cols[1], self.rows[1]),
            (self.cols[2], self.rows[1]),
            (self.cols[0], self.rows[2]),
            (self.cols[1], self.rows[2]),
            (self.cols[2], self.rows[2])
        ]

    def PreprocessForOCR(self, image):
        # convert to black and white
        gray = cv.cvtColor(np.array(image), cv.COLOR_RGB2GRAY)
        _, imgBinary = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
        # fix rotation
        inverted = cv.bitwise_not(imgBinary)
        rotated = imutils.rotate(inverted, -25)
        inverted = cv.bitwise_not(rotated)
        # add border
        top, bottom, left, right = [150]*4
        imgBorder = cv.copyMakeBorder(inverted, top, bottom, left, right,  cv.BORDER_CONSTANT, value=(255, 255, 255))

        return imgBorder

    def DoTask(self):
        x1 = int(round(self.screenSize[0] * 0.646875))
        y1 = int(round(self.screenSize[1] * 0.2722222222222222))
        x2 = int(round(self.screenSize[0] * 0.6958333333333333))
        y2 = int(round(self.screenSize[1] * 0.3287037037037037))

        screenshot = ImageGrab.grab((x1, y1, x2, y2))
        screenshot = self.PreprocessForOCR(screenshot)
        code = pytesseract.image_to_string(screenshot)
        code = "".join(filter(str.isdigit, code))

        for number in code:
            win32api.SetCursorPos(self.buttonPositions[int(number)])
            sleep(0.02)
            Task.Click()
            sleep(0.01)

        buttonEnter = (self.cols[2], self.rows[3])
        win32api.SetCursorPos(buttonEnter)
        sleep(0.02)
        Task.Click()
        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(self.screenSize[0] * 0.7322916666666667)), int(round(self.screenSize[1] * 0.4009259259259259))))
        if self.vision.PixelMatchesColor(pixel, (181, 165, 68)):
            return True
        return False
