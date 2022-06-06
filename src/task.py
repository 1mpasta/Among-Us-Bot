from abc import ABC, abstractmethod
from vision import Vision
import win32api
import win32con
from time import sleep


class Task(ABC):
    vision = Vision()
    screenSize = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

    def Click(delay=0.01):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    @abstractmethod
    def DoTask():
        pass

    @abstractmethod
    def CheckTask():
        pass
