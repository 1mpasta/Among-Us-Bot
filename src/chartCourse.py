from time import sleep

import cv2 as cv
import numpy as np
import win32api
import win32con
from PIL import ImageGrab

from task import Task
from utility import Utility


class ChartCourse(Task):
    def __init__(self):
        self.mask = cv.imread(Utility.resource_path("media\\Chart_Course\\mask.png"), cv.IMREAD_GRAYSCALE)
        self.mask = Utility.resize_to_screen(self.mask, Utility.screenSize, (0.5901041666666667, 0.6324074074074074))

        self.x1 = int(round(Utility.screenSize[0] * 0.2046875))
        self.y1 = int(round(Utility.screenSize[1] * 0.1833333333333333))
        self.x2 = int(round(Utility.screenSize[0] * 0.7947916666666667))
        self.y2 = int(round(Utility.screenSize[1] * 0.8157407407407407))

    def process_image(self, image):
        gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        _, img_bw = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
        img_bw[self.mask > 0] = 0

        kernel = np.ones((2, 2))
        no_noise = cv.erode(img_bw, kernel, iterations=3, borderType=cv.BORDER_CONSTANT)

        kernel2 = np.ones((20, 20))
        blobs = cv.dilate(no_noise, kernel2, iterations=3, borderType=cv.BORDER_CONSTANT)

        contours, _ = cv.findContours(blobs, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        positions = []
        for contour in contours:
            bounding_rect = cv.boundingRect(contour)
            center_x = (bounding_rect[0] + bounding_rect[2] // 2) + self.x1
            center_y = (bounding_rect[1] + bounding_rect[3] // 2) + self.y1

            positions.append((center_x, center_y))

        return positions

    def do_task(self):
        screenshot = np.array(ImageGrab.grab((self.x1, self.y1, self.x2, self.y2)))

        positions = sorted(self.process_image(screenshot))

        win32api.SetCursorPos(positions[0])
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.02)
        for pos in positions:
            win32api.SetCursorPos(pos)
            sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.7552083333333333)), int(round(Utility.screenSize[1] * 0.2481481481481481))))
        if Utility.pixel_matches_color(pixel, (55, 153, 220)):
            return True
        return False
