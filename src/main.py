from time import sleep
import keyboard
import win32api, win32con

from download import Download
from unlockManifolds import UnlockManifolds
from startReactor import StartReactor
from stabilizeSteering import StabilizeSteering
from wires import Wires
from acceptDivertedPower import DivertPowerAccept

wires = Wires()
divertPower = DivertPowerAccept()
stabilizeSteering = StabilizeSteering()
download = Download()
reactor = StartReactor()
manifolds = UnlockManifolds()

# region main
sleep(1)
while keyboard.is_pressed("0") != True:
    sleep(0.01)
    if wires.CheckTask():
        wires.DoTask()
    if divertPower.CheckTask():
        divertPower.DoTask()
    if stabilizeSteering.CheckTask():
        stabilizeSteering.DoTask()
    if download.CheckTask():
        download.DoTask()
    if reactor.CheckTask():
        reactor.DoTask()
    if manifolds.CheckTask():
        manifolds.DoTask()
# endregion
