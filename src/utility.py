import os
import sys
from time import sleep

import cv2 as cv
import win32api
import win32con


class Utility:
    screenSize = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

    @staticmethod
    def click(delay=0.01):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    @staticmethod
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)

        return os.path.join(os.path.abspath(""), relative_path)

    @staticmethod
    def get_location_from_image(needle, haystack, method=cv.TM_CCOEFF_NORMED):

        result = cv.matchTemplate(haystack, needle, method)

        _, _, _, max_loc = cv.minMaxLoc(result)
        click_point = (max_loc[0] + int(needle.shape[1] / 2), max_loc[1] + int(needle.shape[0] / 2))

        return click_point

    @staticmethod
    def pixel_matches_color(pixel, rgb):
        red_ok = pixel[0] >= rgb[0]
        g_red = max(int(round(rgb[1] * 0.62162162162162)), 0)
        green_ok = bool(pixel[1] == rgb[1] or pixel[1] in range(g_red - 1, g_red + 2))
        b_red = max(int(round(rgb[2] * 0.62162162162162)), 0)
        blue_ok = bool(pixel[2] == rgb[2] or pixel[2] in range(b_red - 1, b_red + 2))
        all_ok = bool(red_ok and green_ok and blue_ok)
        if all_ok:
            return True
        return False

    @staticmethod
    def resize_to_screen(src, screensize, percentage):
        size = (int(round(screensize[0] * percentage[0])), int(round(screensize[1] * percentage[1])))
        resized = cv.resize(src, size, cv.INTER_LINEAR)
        return resized
