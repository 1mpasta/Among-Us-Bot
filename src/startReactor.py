from time import sleep
from task import Task
from vision import Vision
from PIL import ImageGrab
import win32api


class StartReactor(Task):

    def __init__(self, screenSize):
        self.vision = Vision()
        self.screenSize = screenSize
        self.sequence = []

    def DoTask(self):
        screenX = int(round(self.screenSize[0] * 0.2604166666666667))
        screenY = int(round(self.screenSize[1] * 0.462962962962963))
        screenMultiplier = int(round(self.screenSize[0] * 0.0598958333333333))
        keypadMultiplier = int(round(self.screenSize[0] * 0.0651041666666667))
        keypadCorner = ((int(round(self.screenSize[0] * 0.5911458333333333)), int(round(self.screenSize[1] * 0.4398148148148148))))

        screenshot = ImageGrab.grab()
        checkPixel = screenshot.getpixel(keypadCorner)

        self.sequence.clear()
        while self.vision.PixelMatchesColor(checkPixel, (104, 104, 104)):
            screenshot = ImageGrab.grab()
            checkPixel = screenshot.getpixel(keypadCorner)
            for x in range(0, 3, 1):
                for y in range(0, 3, 1):
                    tilePixel = screenshot.getpixel((screenX + x * screenMultiplier, screenY + y * screenMultiplier))
                    if self.vision.PixelMatchesColor(tilePixel, (68, 168, 255)):
                        self.sequence.append((x, y))
                        while self.vision.PixelMatchesColor(tilePixel, (68, 168, 255)):
                            screenshot = ImageGrab.grab()
                            tilePixel = screenshot.getpixel((screenX + x * screenMultiplier, screenY + y * screenMultiplier))
                        break
        sleep(0.01)
        for i in self.sequence:
            sleep(0.01)
            win32api.SetCursorPos((keypadCorner[0] + (i[0] * keypadMultiplier), keypadCorner[1] + (i[1] * keypadMultiplier)))
            sleep(0.02)
            Task.Click()
            sleep(0.02)

    def CheckTask(self, screenshot):
        pixel = screenshot.getpixel((int(round(self.screenSize[0] * 0.8083333333333333)), int(round(self.screenSize[1] * 0.2259259259259259))))
        if self.vision.PixelMatchesColor(pixel, (66, 65, 66)):
            return True
        return False
