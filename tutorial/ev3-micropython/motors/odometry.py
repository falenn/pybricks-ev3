#!/usr/bin/env pybricks-micropython
''' Given our robot configuration, drive forward a distance '''
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math
from time import sleep

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()

# Initialize a motor at port B
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
wheel_diam = 55.5
axle_track = 104.4
radius = wheel_diam/2

robot = DriveBase(left_motor, right_motor, wheel_diam, axle_track)

# Circumference -> c=2Pir 
# r = radius
# Pi = 3.14159
circ = 2 * math.pi * radius
def rotations_to_mm(rotations):
    return rotations * circ

# Circumference is distance travelled in 1 rotation
def mm_to_rotations(distance_in_mm=100):
    ''' travel calc in millimeters
        distance_in_mm = 10 cm is default
        return rotations
    '''
    return distance_in_mm / circ

def cm_to_rotations(distance_in_cm=10):
    ''' travel calc in millimeters
        distance_in_mm = 10 cm is default
        return rotations
    '''
    return (distance_in_cm / circ)/10

def drive(rotations=0, speed=35):
    print(F"Move robot {rotations} rotations")
    angle = rotations*360
    right_motor.run_target(speed, angle)
    left_motor.run_target(speed, angle)

def drive_cm(distance_in_cm=0, speed=35, turn_rate=0):
    ''' Drive the robot so many rotations'''
    global circ
    circ_cm=circ/10
    print(F"Move robot {distance_in_cm} cm")
    rotations = distance_in_cm/circ_cm
    drive(speed,rotations)

if __name__ == "__main__":
    drive(1) # should be 1 rotation
    drive_cm(10) # should be about 1 rotation
