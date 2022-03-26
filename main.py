from msilib import sequence
from time import sleep
import keyboard
import pyautogui
import win32api
import win32con

def Click(delay=0.01):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# region wires
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


def GetWireColors():
    wireColors.clear()
    # loop through wires
    for wire in wiresYPositons:
        # loop through colors
        for color in colors:
            if pyautogui.pixelMatchesColor(left, wire, color):
                wireColors.append(colors.index(color))
                break
    if len(wireColors) < 4:
        print("ERROR: wires not found")
    print(wireColors)


def ConnectWires():
    i = 0
    for wire in wireColors:
        sleep(0.02)
        win32api.SetCursorPos((left, wiresYPositons[i]))
        sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,
                             left, wiresYPositons[i])
        sleep(0.02)
        win32api.SetCursorPos((right, wiresYPositons[wire]))
        sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,
                             right, wiresYPositons[wire])
        sleep(0.02)
        i = i + 1


def DoWires():
    GetWireColors()
    ConnectWires()
    keyboard.press_and_release("esc")


def CheckWires():
    if pyautogui.pixelMatchesColor(1407, 257, (165, 0, 0)):
        return True
    return False
# endregion

# region divertPowerAccept

# x960 y550


def DoDivertPowerAccept():
    win32api.SetCursorPos((960, 550))
    sleep(0.01)
    Click()
    sleep(0.03)
    keyboard.press_and_release("esc")


def CheckDivertPowerAccept():
    if pyautogui.pixelMatchesColor(530, 560, (127, 90, 0)):
        return True
    return False
# endregion

# region stabilizeSteering


def DoStabilizeSteering():
    win32api.SetCursorPos((960, 540))
    sleep(0.01)
    Click()
    sleep(0.01)
    keyboard.press_and_release("esc")


def CheckStabilizeSteering():
    if pyautogui.pixelMatchesColor(960, 140, (14, 63, 95)):
        return True
    return False

# endregion

# region download/upload


def DoDownload():
    win32api.SetCursorPos((960, 660))
    sleep(0.01)
    Click()
    sleep(0.5)


def CheckDownload():
    if pyautogui.pixelMatchesColor(1447, 222, (78, 112, 148)):
        return True
    return False
# endregion

# region reactor

sequence = []

def DoReactor():
    sequence.clear()
    while pyautogui.pixelMatchesColor(1135, 470, (104, 104, 104)):
        pic = pyautogui.screenshot(None, region=(500, 500, 500, 500))
        for x in range(0, 3, 1):
            for y in range(0, 3, 1):
                rgb = pic.getpixel((x*115, y*115))
                if rgb == (68, 168, 255):
                    sequence.append((x, y))
                    sleep(0.2)

    for i in sequence:
        win32api.SetCursorPos((1135+(i[0]*125), 475+(i[1]*125)))
        sleep(0.01)
        Click()
        sleep(0.1)
    
def CheckReactor():
    if pyautogui.pixelMatchesColor(1552, 244, (66, 65, 66)):
        return True
    return False

    # endregion

# region main
sleep(1)
while keyboard.is_pressed("0") != True:
    sleep(0.01)
    if CheckWires():
        DoWires()
    if CheckDivertPowerAccept():
        DoDivertPowerAccept()
    if CheckStabilizeSteering():
        DoStabilizeSteering()
    if CheckDownload():
        DoDownload()
    if CheckReactor():
        DoReactor()
# endregion