from time import sleep
from task import Task
from vision import Vision
from PIL import ImageGrab
import cv2 as cv
import numpy as np
import keyboard
import win32api
import win32con


class DivertPower(Task):

    def __init__(self, screenSize):
        self.vision = Vision()
        self.screenSize = screenSize
        self.slider = cv.imread("media/Divert_Power/slider.png", cv.IMREAD_COLOR)
        self.slider = self.vision.ResizeToScreen(self.slider, screenSize, (0.0432291666666667, 0.0601851851851852))

    def DoTask(self):
        sleep(0.03)

        corner = (int(round(self.screenSize[0] * 0.3020833333333333)), int(round(self.screenSize[1] * 0.6972222222222222)))
        region = (corner[0], corner[1], corner[0] + int(round(self.screenSize[0] * 0.3958333333333333)), corner[1] + int(round(self.screenSize[1] * 0.062037037037037)))
        screenshot = ImageGrab.grab(region)
        screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

        clickPoint = self.vision.GetLocationFromPicture(self.slider, screenshot)
        clickPoint = (clickPoint[0] + corner[0], clickPoint[1] + corner[1])

        win32api.SetCursorPos(clickPoint)
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.02)
        win32api.SetCursorPos((clickPoint[0], 10))
        sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        sleep(0.01)
        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(self.screenSize[0] * 0.684375)), int(round(self.screenSize[1] * 0.4259259259259259))))
        if self.vision.PixelMatchesColor(pixel, (253, 255, 92)):
            return True
        return False
