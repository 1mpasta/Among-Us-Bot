from time import sleep
import keyboard
import pyautogui
import win32api
import win32con

#region wires
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
#endregion

#region divertPowerAccept

# x960 y550

def DoDivertPowerAccept():
    win32api.SetCursorPos((960,550))
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,960,550)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,960,550)
    sleep(0.03)
    keyboard.press_and_release("esc")
    
def CheckDivertPowerAccept():
    if pyautogui.pixelMatchesColor(530, 560, (127, 90, 0)):
        return True
    return False
#endregion

#region main
sleep(1)
while keyboard.is_pressed("0") != True:
    sleep(0.01)
    if CheckWires():
        DoWires()
    if CheckDivertPowerAccept():
        DoDivertPowerAccept()
#endregion