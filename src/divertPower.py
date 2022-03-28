from time import sleep
from task import Task
from vision import Vision
import cv2 as cv
import numpy as np
import keyboard
import pyautogui
import win32api, win32con

class DivertPower(Task):
    
    slider = cv.imread("media/Divert_Power/slider.png", cv.IMREAD_COLOR)
    vision = Vision()
    
    def DoTask(self):
        screenshot = pyautogui.screenshot(region=(580, 753, 760, 67))
        
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        
        clickPoint = self.vision.GetLocationFromPicture(self.slider, screenshot)
        clickPoint = (clickPoint[0] + 580, clickPoint[1] + 753)
        
        win32api.SetCursorPos(clickPoint)
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.02)
        win32api.SetCursorPos((clickPoint[0], clickPoint[1] - 200))
        sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        sleep(0.01)
        keyboard.press_and_release("esc")
    
    def CheckTask(self):
        if pyautogui.pixelMatchesColor(1314, 460, (253, 255, 92)):
            return True
        return False