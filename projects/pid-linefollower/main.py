#!/usr/bin/env pybricks-micropython
'''line-follower'''
from pybricks.parameters import Port
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
import robotics.pid as PID
    
target = 27
# Set the drive speed at 100 millimeters per second.
drivespeed=30
kp=.5
ki=.05
kd=.5
side=1  #1 for left, or -1 for right side of line

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
# https://pybricks.github.io/ev3-micropython/robotics.html
robot = DriveBase(left_motor, right_motor, 55.5, 104)
cs = ColorSensor(Port.S3)

# Create PID for color sensor, on left side of line
pid = PID.PID(target, kp,ki,kd,side)

# Start driving, turning away from the line to follow
robot.drive(drivespeed, 0)

while True:
    print("light: ", cs.reflection())
    correction = pid.calc(current=cs.reflection())
    print("current: ", cs.reflection(), "target: ", target, "PID: ", correction)
    robot.drive(drivespeed, correction)
    pid.displayStatus()
    wait(10)

