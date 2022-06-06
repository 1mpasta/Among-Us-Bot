from time import sleep
from task import Task
import keyboard
import win32api


class StabilizeSteering(Task):

    def DoTask(self):
        win32api.SetCursorPos((Task.screenSize[0] // 2, Task.screenSize[1] // 2))
        sleep(0.01)
        Task.Click()
        sleep(0.02)
        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((Task.screenSize[0] // 2, int(round(Task.screenSize[1] * 0.1296296296296296))))
        pixel2 = screenshot.getpixel((Task.screenSize[0] // 2, int(round(Task.screenSize[1] * 0.8666666666666667))))
        if Task.vision.PixelMatchesColor(pixel, (14, 63, 95)) and Task.vision.PixelMatchesColor(pixel2, (14, 63, 95)):
            return True
        return False
