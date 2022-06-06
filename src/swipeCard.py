from task import Task
from time import sleep
from PIL import ImageGrab
import keyboard
import win32api
import win32con


class SwipeCard(Task):

    def __init__(self):
        self.swipeTime = 0.05
        self.segments = 25
        self.startX = int(round(Task.screenSize[0] * 0.2890625))
        self.endX = int(round(Task.screenSize[0] * 0.7552083333333333))
        self.y = int(round(Task.screenSize[1] * 0.3796296296296296))

    def DoTask(self):
        win32api.SetCursorPos((int(round(Task.screenSize[0] * 0.390625)), int(round(Task.screenSize[1] * 0.7962962962962963))))
        sleep(0.01)
        Task.Click()

        pixelPos = (int(round(Task.screenSize[0] * 0.7005208333333333)), int(round(Task.screenSize[1] * 0.3009259259259259)))
        screenshot = ImageGrab.grab()
        pixel = screenshot.getpixel(pixelPos)
        while Task.vision.PixelMatchesColor(pixel, (0, 99, 71)):
            screenshot = ImageGrab.grab()
            pixel = screenshot.getpixel(pixelPos)

        win32api.SetCursorPos((self.startX, self.y))
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.02)
        for i in range(1, self.segments + 1):
            nextPos = self.startX + int(((self.endX - self.startX) // self.segments) * i)
            win32api.SetCursorPos((nextPos, self.y))
            sleep(self.swipeTime / self.segments)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(Task.screenSize[0] * 0.690625)), int(round(Task.screenSize[1] * 0.1166666666666667))))
        pixel2 = screenshot.getpixel((int(round(Task.screenSize[0] * 0.6770833333333333)), int(round(Task.screenSize[1] * 0.8611111111111111))))
        if Task.vision.PixelMatchesColor(pixel, (22, 74, 57)) and Task.vision.PixelMatchesColor(pixel2, (71, 147, 52)):
            return True
        return False
