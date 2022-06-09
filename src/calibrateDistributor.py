from time import sleep

import keyboard
import win32api
from PIL import ImageGrab

from task import Task
from utility import Utility


class CalibrateDistributor(Task):
    def __init__(self):
        self.x = int(round(Utility.screenSize[0] * 0.6380208333333333))
        self.screen_y = int(round(Utility.screenSize[1] * 0.212962962962963))
        self.button_y = int(round(Utility.screenSize[1] * 0.2962962962962963))
        self.screen_multiplier = int(round(Utility.screenSize[1] * 0.25))
        self.button_multiplier = int(round(Utility.screenSize[1] * 0.2407407407407407))

    def do_task(self):
        screenshot = ImageGrab.grab()

        pixel = screenshot.getpixel((self.x, self.screen_y))
        while Utility.pixel_matches_color(pixel, (0, 0, 0)):
            screenshot = ImageGrab.grab()
            pixel = screenshot.getpixel((self.x, self.screen_y))

        win32api.SetCursorPos((self.x, self.button_y))
        sleep(0.01)
        Utility.click()

        pixel = screenshot.getpixel((self.x, self.screen_y + self.screen_multiplier))
        while Utility.pixel_matches_color(pixel, (0, 0, 0)):
            screenshot = ImageGrab.grab()
            pixel = screenshot.getpixel((self.x, self.screen_y + self.screen_multiplier))

        win32api.SetCursorPos((self.x, self.button_y + self.button_multiplier))
        sleep(0.01)
        Utility.click()

        pixel = screenshot.getpixel((self.x, self.screen_y + (self.screen_multiplier * 2)))
        while Utility.pixel_matches_color(pixel, (0, 0, 0)):
            screenshot = ImageGrab.grab()
            pixel = screenshot.getpixel((self.x, self.screen_y + (self.screen_multiplier * 2)))

        win32api.SetCursorPos((self.x, self.button_y + (self.button_multiplier * 2)))
        sleep(0.01)
        Utility.click()
        sleep(0.01)
        keyboard.press_and_release("esc")

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.5828125)), int(round(Utility.screenSize[1] * 0.1962962962962963))))
        if Utility.pixel_matches_color(pixel, (255, 227, 0)):
            return True
        return False
