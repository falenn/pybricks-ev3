#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.nxtdevices import TouchSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
wheel_diam=38.1 # in mm
axle_track=114.3 # in mm

# Create your objects here.
ev3 = EV3Brick()

# Initialize a motor at port B
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
touch = TouchSensor(Port.S1)


# turn the left motor 90 degrees @ 100 deg/sec - 
# put the white flag on the wheel axle to see the rotation better
left_motor.run_target(100,90)

ev3.speaker.beep(1000, 500)

# Initialize the drive base.
robot = DriveBase(left_motor, \
    right_motor, wheel_diameter=wheel_diam, axle_track=axle_track)

if __name__ == "__main__":    
    is_touched = False
    while True:
        if not is_touched:
            robot.straight(10)
        else:
            robot.stop()
        is_touched = touch.pressed
        wait(1)
        



    