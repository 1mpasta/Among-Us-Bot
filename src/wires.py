from time import sleep

import keyboard
import win32api
import win32con
from PIL import ImageGrab

from task import Task
from utility import Utility


class Wires(Task):
    def __init__(self):
        self.wires_left, self.wires_right = int(round(Utility.screenSize[0] * 0.2942708333333333)), int(round(Utility.screenSize[0] * 0.6901041666666667))
        self.wires_y = [
            int(round(Utility.screenSize[1] * 0.25)),
            int(round(Utility.screenSize[1] * 0.4259259259259259)),
            int(round(Utility.screenSize[1] * 0.5972222222222222)),
            int(round(Utility.screenSize[1] * 0.7685185185185185)),
        ]
        self.wire_colors = [(255, 0, 0), (38, 38, 255), (255, 235, 4), (255, 0, 255)]
        self.wire_order = []

    def get_wire_colors(self):
        self.wire_order.clear()
        screenshot = ImageGrab.grab()

        for color in self.wire_colors:
            for i, wire in enumerate(self.wires_y):
                pixel = screenshot.getpixel((self.wires_left, wire))
                if Utility.pixel_matches_color(pixel, color):
                    self.wire_order.append(i)
                    break

    def connect_wires(self):
        for i, wire in enumerate(self.wire_order):
            win32api.SetCursorPos((self.wires_left, self.wires_y[wire]))
            sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            sleep(0.02)
            win32api.SetCursorPos((self.wires_right, self.wires_y[i]))
            sleep(0.02)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            sleep(0.01)

    def do_task(self):
        self.get_wire_colors()
        if len(self.wire_order) < 4:
            return
        self.connect_wires()
        keyboard.press_and_release("esc")

    def check_task(self, screenshot):
        pixel = screenshot.getpixel((int(round(Utility.screenSize[0] * 0.7328125)), int(round(Utility.screenSize[1] * 0.237962962962963))))
        if Utility.pixel_matches_color(pixel, (165, 0, 0)):
            return True
        return False
