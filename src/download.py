from time import sleep
from task import Task
import win32api


class Download(Task):

    def DoTask(self):
        win32api.SetCursorPos((Task.screenSize[0] // 2, int(round(Task.screenSize[1] * 0.6111111111111111))))
        sleep(0.01)
        Task.Click()
        sleep(0.5)

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(Task.screenSize[0] * 0.7536458333333333)), int(round(Task.screenSize[1] * 0.2055555555555556))))
        if Task.vision.PixelMatchesColor(pixel, (78, 112, 148)):
            return True
        return False
