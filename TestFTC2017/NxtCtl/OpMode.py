#import inputs
import nxt, time, thread, threading, Range
from GamePad import *
from GameGraphics import TextDisplay

telemetry = TextDisplay("Robot Telemetry")

def init():
    pass
def init_loop():
    pass
def loop():
    pass

def run():
    init()
    init_loop()
    while 1:
        loop()
        padDisplay.reset()
        gamepad1.show_status()
        gamepad2.show_status()
        gamepad3.show_status()
        gamepad4.show_status()
        time.sleep(.01)
run()
