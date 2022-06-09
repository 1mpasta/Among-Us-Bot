from time import sleep

import win32api
from PIL import ImageGrab

from task import Task
from utility import Utility


class StartReactor(Task):
    def __init__(self):
        self.sequence = []

    def do_task(self):
        screen_x = int(round(Utility.screenSize[0] * 0.2604166666666667))
        screen_y = int(round(Utility.screenSize[1] * 0.462962962962963))
        screen_multiplier = int(round(Utility.screenSize[0] * 0.0598958333333333))
        keypad_multiplier = int(round(Utility.screenSize[0] * 0.0651041666666667))
        keypad_corner = (int(round(Utility.screenSize[0] * 0.5911458333333333)), int(round(Utility.screenSize[1] * 0.4398148148148148)))

        screenshot = ImageGrab.grab()
        check_pixel = screenshot.getpixel(keypad_corner)

        self.sequence.clear()
        while Utility.pixel_matches_color(check_pixel, (104, 104, 104)):
            screenshot = ImageGrab.grab()
            check_pixel = screenshot.getpixel(keypad_corner)
            for x in range(0, 3, 1):
                for y in range(0, 3, 1):
                    tile_pixel = screenshot.getpixel((screen_x + x * screen_multiplier, screen_y + y * screen_multiplier))
                    if Utility.pixel_matches_color(tile_pixel, (68, 168, 255)):
                        self.sequence.append((x, y))
                        while Utility.pixel_matches_color(tile_pixel, (68, 168, 255)):
                            screenshot = ImageGrab.grab()
                            tile_pixel = screenshot.getpixel((screen_x + x * screen_multiplier, screen_y + y * screen_multiplier))
                        break
        sleep(0.01)
        for i in self.sequence:
            sleep(0.01)
            win32api.SetCursorPos((keypad_corner[0] + (i[0] * keypad_multiplier), keypad_corner[1] + (i[1] * keypad_multiplier)))
            sleep(0.02)
            Utility.click()
            sleep(0.02)

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.8083333333333333)), int(round(Utility.screenSize[1] * 0.2259259259259259))))
        if Utility.pixel_matches_color(pixel, (66, 65, 66)):
            return True
        return False
