from task import Task
from time import sleep
from PIL import ImageGrab
import cv2 as cv
import numpy as np
import win32api
import win32con


class ChartCourse(Task):

    def __init__(self):
        self.mask = cv.imread("media/Chart_Course/mask.png", cv.IMREAD_GRAYSCALE)
        self.mask = Task.vision.ResizeToScreen(self.mask, Task.screenSize, (0.5901041666666667, 0.6324074074074074))

        self.x1 = int(round(Task.screenSize[0] * 0.2046875))
        self.y1 = int(round(Task.screenSize[1] * 0.1833333333333333))
        self.x2 = int(round(Task.screenSize[0] * 0.7947916666666667))
        self.y2 = int(round(Task.screenSize[1] * 0.8157407407407407))

    def ProcessImage(self, image):
        gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        _, imgBW = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
        imgBW[self.mask > 0] = 0

        kernel = np.ones((2, 2))
        noiseRemoved = cv.erode(imgBW, kernel, iterations=3, borderType=cv.BORDER_CONSTANT)

        kernel2 = np.ones((20, 20))
        blobs = cv.dilate(noiseRemoved, kernel2, iterations=3, borderType=cv.BORDER_CONSTANT)

        contours, _ = cv.findContours(blobs, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        positions = []
        for contour in contours:
            br = cv.boundingRect(contour)
            cx = (br[0] + br[2] // 2) + self.x1
            cy = (br[1] + br[3] // 2) + self.y1

            positions.append((cx, cy))

        return positions

    def DoTask(self):
        screenshot = np.array(ImageGrab.grab((self.x1, self.y1, self.x2, self.y2)))

        positions = sorted(self.ProcessImage(screenshot))

        win32api.SetCursorPos(positions[0])
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.02)
        for pos in positions:
            win32api.SetCursorPos(pos)
            sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(Task.screenSize[0] * 0.7552083333333333)), int(round(Task.screenSize[1] * 0.2481481481481481))))
        if Task.vision.PixelMatchesColor(pixel, (55, 153, 220)):
            return True
        return False
