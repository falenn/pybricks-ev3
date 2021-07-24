from pybricks.hubs import EV3Brick
import os

ev3 = EV3Brick()

def health():
    global ev3
    ev3.screen.print("Power: ",ev3.battery.voltage())


    