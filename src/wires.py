from time import sleep
import keyboard
import win32api
import win32con
from task import Task
from PIL import ImageGrab


class Wires(Task):

    def __init__(self):
        self.wiresLeft, self.wiresRight = int(round(Task.screenSize[0] * 0.2942708333333333)), int(round(Task.screenSize[0] * 0.6901041666666667))
        self.wiresYPositons = [
            int(round(Task.screenSize[1] * 0.25)),
            int(round(Task.screenSize[1] * 0.4259259259259259)),
            int(round(Task.screenSize[1] * 0.5972222222222222)),
            int(round(Task.screenSize[1] * 0.7685185185185185))
        ]
        self.wireColors = [
            (255, 0, 0),
            (38, 38, 255),
            (255, 235, 4),
            (255, 0, 255)
        ]
        self.wireOrder = []

    def GetWireColors(self):
        self.wireOrder.clear()
        screenshot = ImageGrab.grab()

        for color in self.wireColors:
            for i, wire in enumerate(self.wiresYPositons):
                pixel = screenshot.getpixel((self.wiresLeft, wire))
                if Task.vision.PixelMatchesColor(pixel, color):
                    self.wireOrder.append(i)
                    break

    def ConnectWires(self):
        for i, wire in enumerate(self.wireOrder):
            win32api.SetCursorPos((self.wiresLeft, self.wiresYPositons[wire]))
            sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            sleep(0.02)
            win32api.SetCursorPos((self.wiresRight, self.wiresYPositons[i]))
            sleep(0.02)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            sleep(0.01)

    def DoTask(self):
        self.GetWireColors()
        if len(self.wireOrder) < 4:
            return
        self.ConnectWires()
        keyboard.press_and_release("esc")

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(Task.screenSize[0] * 0.7328125)), int(round(Task.screenSize[1] * 0.237962962962963))))
        if Task.vision.PixelMatchesColor(pixel, (165, 0, 0)):
            return True
        return False
