from time import sleep
from task import Task
import keyboard
import win32api
import win32con


class EmptyGarbage(Task):

    def DoTask(self):
        win32api.SetCursorPos((int(round(Task.screenSize[0] * 0.6614583333333333)), int(round(Task.screenSize[1] * 0.3888888888888889))))
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.02)
        win32api.SetCursorPos((int(round(Task.screenSize[0] * 0.6614583333333333)), int(round(Task.screenSize[1] * 0.8333333333333333))))
        sleep(1.35)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        sleep(0.03)
        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(Task.screenSize[0] * 0.625)), int(round(Task.screenSize[1] * 0.4675925925925926))))
        if Task.vision.PixelMatchesColor(pixel, (145, 175, 187)):
            return True
        return False
