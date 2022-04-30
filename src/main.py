from time import sleep
import keyboard
import win32api
from PIL import ImageGrab

from divertPower import DivertPower
from download import Download
from fuelEngines import FuelEngines
from unlockManifolds import UnlockManifolds
from startReactor import StartReactor
from stabilizeSteering import StabilizeSteering
from wires import Wires
from acceptDivertedPower import DivertPowerAccept

screenSize = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

wires = Wires(screenSize)
divertPowerAccept = DivertPowerAccept(screenSize)
stabilizeSteering = StabilizeSteering(screenSize)
download = Download(screenSize)
reactor = StartReactor(screenSize)
manifolds = UnlockManifolds(screenSize)
divertPower = DivertPower(screenSize)
fuelEngines = FuelEngines(screenSize)

taskList = [
    wires,
    divertPower,
    divertPowerAccept,
    stabilizeSteering,
    download,
    reactor,
    manifolds,
    fuelEngines
]

# region main
sleep(1)
while not keyboard.is_pressed("0"):
    screenshot = ImageGrab.grab()

    for task in taskList:
        if task.CheckTask(screenshot):
            task.DoTask()
# endregion
