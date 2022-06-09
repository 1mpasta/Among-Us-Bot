import time

import keyboard
from PIL import ImageGrab

from acceptDivertedPower import DivertPowerAccept
from calibrateDistributor import CalibrateDistributor
from chartCourse import ChartCourse
from divertPower import DivertPower
from download import Download
from emptyGarbage import EmptyGarbage
from fuelEngines import FuelEngines
from sabotageLights import SabotageLights
from sabotageO2 import SabotageO2
from stabilizeSteering import StabilizeSteering
from startReactor import StartReactor
from swipeCard import SwipeCard
from unlockManifolds import UnlockManifolds
from wires import Wires

divertPowerAccept = DivertPowerAccept()
calibrateDistributor = CalibrateDistributor()
chartCourse = ChartCourse()
divertPower = DivertPower()
download = Download()
emptyGarbage = EmptyGarbage()
fuelEngines = FuelEngines()
sabotageLights = SabotageLights()
sabotageO2 = SabotageO2()
stabilizeSteering = StabilizeSteering()
startReactor = StartReactor()
swipeCard = SwipeCard()
unlockManifolds = UnlockManifolds()
wires = Wires()

taskList = [
    divertPowerAccept,
    calibrateDistributor,
    chartCourse,
    divertPower,
    download,
    emptyGarbage,
    fuelEngines,
    sabotageO2,
    stabilizeSteering,
    startReactor,
    swipeCard,
    unlockManifolds,
    wires
]
def main():
    impostor_mode = False

    time.sleep(1)
    print("Started")
    while not keyboard.is_pressed("f12"):
        screenshot = ImageGrab.grab()

        if keyboard.is_pressed("f11"):
            impostor_mode = not impostor_mode
            time.sleep(0.1)

        if not impostor_mode:
            for task in taskList:
                if task.check_task(screenshot):
                    # screenshot.save(f"TEST/{task.__class__.__name__}{time.time()}.png")
                    task.do_task()

        if sabotageLights.check_task(screenshot):
            sabotageLights.do_task(impostor_mode)

if __name__ == "__main__":
    main()
