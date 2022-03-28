from time import sleep
import keyboard
import pyautogui
import win32api, win32con
from task import Task

class Wires(Task):

    """
        # wire positions
        # left  x 565
        # right x 1325
        # y 270
        # y 460
        # y 645
        # y 830

        # colors
        # red    255   0   0
        # blue   38   38 255
        # yellow 255 235   4
        # pink   255   0 255
"""

    left = 565
    right = 1325
    wiresYPositons = [270, 460, 645, 830]
    colors = [
    (255, 0, 0),
    (38, 38, 255),
    (255, 235, 4),
    (255, 0, 255)
    ]
    wireColors = []

    def GetWireColors(self):
        self.wireColors.clear()
        # loop through wires
        for wire in self.wiresYPositons:
            # loop through colors
            for color in self.colors:
                if pyautogui.pixelMatchesColor(self.left, wire, color):
                    self.wireColors.append(self.colors.index(color))
                    break
        if len(self.wireColors) < 4:
            print("ERROR: wires not found")

    def ConnectWires(self):
        i = 0
        for wire in self.wireColors:
            sleep(0.02)
            win32api.SetCursorPos((self.left, self.wiresYPositons[i]))
            sleep(0.02)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.left, self.wiresYPositons[i])
            sleep(0.02)
            win32api.SetCursorPos((self.right, self.wiresYPositons[wire]))
            sleep(0.02)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.right, self.wiresYPositons[wire])
            sleep(0.02)
            i = i + 1

    def DoTask(self):
        self.GetWireColors()
        self.ConnectWires()
        keyboard.press_and_release("esc")


    def CheckTask(self):
        if pyautogui.pixelMatchesColor(1407, 257, (165, 0, 0)):
            return True
        return False
    