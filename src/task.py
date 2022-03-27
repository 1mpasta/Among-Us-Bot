from abc import ABC, abstractmethod
import win32api, win32con
from time import sleep

class Task(ABC):
    
    def Click(delay=0.01):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
    @abstractmethod
    def DoTask():
        pass
    
    @abstractmethod
    def CheckTask():
        pass