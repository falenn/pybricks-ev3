#!/usr/bin/env pybricks-micropython
from time import sleep
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop


# Create objects here
ev3 = EV3Brick()
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)

