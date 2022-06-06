from task import Task
from time import sleep
import keyboard
import win32api


class DivertPowerAccept(Task):

    def DoTask(self):
        win32api.SetCursorPos((Task.screenSize[0] // 2, Task.screenSize[1] // 2))
        sleep(0.01)
        Task.Click()
        sleep(0.5)
        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(Task.screenSize[0] * 0.27604166666667)), int(round(Task.screenSize[1] * 0.5185185185185185))))
        if Task.vision.PixelMatchesColor(pixel, (127, 90, 0)):
            return True
        return False
