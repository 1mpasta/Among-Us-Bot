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
from sabotageO2 import SabotageO2
from sabotageLights import SabotageLights
from calibrateDistributor import CalibrateDistributor
from primeShields import PrimeShields

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
primeShields = PrimeShields(screenSize)

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
    primeShields
]

impostorMode = False

# region main
sleep(1)
print("Started")
while not keyboard.is_pressed("f12"):
    screenshot = ImageGrab.grab()

    if keyboard.is_pressed("f11"):
        impostorMode = not impostorMode
        sleep(0.1)

    if not impostorMode:
        for task in taskList:
            if task.CheckTask(screenshot):
                task.DoTask()

    if sabotageLights.CheckTask(screenshot):
        sabotageLights.DoTask(impostorMode)
# endregion
