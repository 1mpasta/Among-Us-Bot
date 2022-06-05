import time
import keyboard
import win32api
from PIL import Image, ImageGrab

from divertPower import DivertPower
from download import Download
from fuelEngines import FuelEngines
from unlockManifolds import UnlockManifolds
from startReactor import StartReactor
from stabilizeSteering import StabilizeSteering
from wires import Wires
from acceptDivertedPower import DivertPowerAccept
from sabotageO2 import SabotageO2
from sabotageLights import SabotageLights
from calibrateDistributor import CalibrateDistributor
from swipeCard import SwipeCard
from emptyGarbage import EmptyGarbage

screenSize = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

wires = Wires(screenSize)
divertPowerAccept = DivertPowerAccept(screenSize)
stabilizeSteering = StabilizeSteering(screenSize)
download = Download(screenSize)
reactor = StartReactor(screenSize)
manifolds = UnlockManifolds(screenSize)
divertPower = DivertPower(screenSize)
fuelEngines = FuelEngines(screenSize)
sabotageO2 = SabotageO2(screenSize)
sabotageLights = SabotageLights(screenSize)
calibrateDistributor = CalibrateDistributor(screenSize)
swipeCard = SwipeCard(screenSize)
emptyGarbage = EmptyGarbage(screenSize)

taskList = [
    wires,
    divertPower,
    divertPowerAccept,
    stabilizeSteering,
    download,
    reactor,
    manifolds,
    fuelEngines,
    sabotageO2,
    calibrateDistributor,
    swipeCard,
    emptyGarbage
]

impostorMode = False

# region main
time.sleep(1)
print("Started")
while not keyboard.is_pressed("f12"):
    screenshot = ImageGrab.grab()

    if keyboard.is_pressed("f11"):
        impostorMode = not impostorMode
        time.sleep(0.1)

    if not impostorMode:
        for task in taskList:
            if task.CheckTask(screenshot):
                # print(str(task))
                # screenshot.save(f"TEST/{time.time()}.png")
                task.DoTask()

    if sabotageLights.CheckTask(screenshot):
        sabotageLights.DoTask(impostorMode)
# endregion
