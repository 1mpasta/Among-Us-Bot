from time import sleep
from task import Task
import pyautogui
import win32api

class StartReactor(Task):

    sequence = []

    def DoTask(self):
        self.sequence.clear()
        while pyautogui.pixelMatchesColor(1135, 470, (104, 104, 104)):
            pic = pyautogui.screenshot(None, region=(500, 500, 500, 500))
            for x in range(0, 3, 1):
                for y in range(0, 3, 1):
                    rgb = pic.getpixel((x*115, y*115))
                    if rgb == (68, 168, 255):
                        self.sequence.append((x, y))
                        sleep(0.25)
        sleep(0.01)
        for i in self.sequence:
            sleep(0.01)
            win32api.SetCursorPos((1135+(i[0]*125), 475+(i[1]*125)))
            sleep(0.02)
            Task.Click()
            sleep(0.2)

    def CheckTask(self):
        if pyautogui.pixelMatchesColor(1552, 244, (66, 65, 66)):
            return True
        return False
    