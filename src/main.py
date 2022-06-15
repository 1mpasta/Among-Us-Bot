import os
import sys
import time

import keyboard
from PIL import ImageGrab
from pytesseract import pytesseract

from acceptDivertedPower import DivertPowerAccept
from calibrateDistributor import CalibrateDistributor
from chartCourse import ChartCourse
from divertPower import DivertPower
from download import Download
from emptyGarbage import EmptyGarbage
from fuelEngines import FuelEngines
from inspectSample import InspectSample
from sabotageLights import SabotageLights
from sabotageO2 import SabotageO2
from stabilizeSteering import StabilizeSteering
from startReactor import StartReactor
from swipeCard import SwipeCard
from unlockManifolds import UnlockManifolds
from utility import Utility
from wires import Wires

divertPowerAccept = DivertPowerAccept()
calibrateDistributor = CalibrateDistributor()
chartCourse = ChartCourse()
divertPower = DivertPower()
download = Download()
emptyGarbage = EmptyGarbage()
fuelEngines = FuelEngines()
inspectSample = InspectSample()
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
    inspectSample,
    sabotageO2,
    stabilizeSteering,
    startReactor,
    swipeCard,
    unlockManifolds,
    wires
]
def main():
    pytesseract.tesseract_cmd = Utility.resource_path("Tesseract-OCR\\tesseract.exe")
    impostor_mode = False

    os.system("cls")
    sys.stdout.write("\033[?25l")

    time.sleep(1)
    while not keyboard.is_pressed("f12"):
        frame_time = time.perf_counter()
        screenshot = ImageGrab.grab()

        if keyboard.is_pressed("f10"):
            impostor_mode = not impostor_mode
            time.sleep(0.1)

        if not impostor_mode:
            for task in taskList:
                if task.check_task(screenshot):
                    # screenshot.save(f"TEST/{task.__class__.__name__}{time.time()}.png")
                    task.do_task()

        if sabotageLights.check_task(screenshot):
            sabotageLights.do_task(impostor_mode)

        draw_ui(frame_time, impostor_mode)

    os.system("cls")
    sys.stdout.write("\033[?25h")

def draw_ui(frame_time, impostor_mode):
    sys.stdout.write("\033[?25l")

    title = "----------[Among Us Task Bot]----------"
    sys.stdout.write(f"{title}\n")

    fps = f"[FPS: {int(60 / (time.perf_counter() - frame_time))}]"
    line = "-" * ((len(title) - len(fps)) // 2)
    extra = "-" if len(line + fps + line) < len(title) else ""
    sys.stdout.write(f"{line}{fps}{line}{extra}\n")

    impostor_status = "\033[30;42mON " if impostor_mode else "\033[30;41mOFF"
    sys.stdout.write(f"  ImpostorMode: {impostor_status}\033[0m\n")

    sys.stdout.write("\n")

    sys.stdout.write("  Keybinds:\n")
    sys.stdout.write(
        "    [F10] - Toggle ImpostorMode\n" +
        "    [F12] - Exit\n"
        )

    sys.stdout.write("\033[7A")

if __name__ == "__main__":
    main()
