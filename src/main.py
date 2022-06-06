import time
import keyboard
from PIL import ImageGrab

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


wires = Wires()
divertPowerAccept = DivertPowerAccept()
stabilizeSteering = StabilizeSteering()
download = Download()
reactor = StartReactor()
manifolds = UnlockManifolds()
divertPower = DivertPower()
fuelEngines = FuelEngines()
sabotageO2 = SabotageO2()
sabotageLights = SabotageLights()
calibrateDistributor = CalibrateDistributor()
swipeCard = SwipeCard()
emptyGarbage = EmptyGarbage()

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
