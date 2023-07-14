#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.nxtdevices import TouchSensor
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

""" Initialize the robot drive base"""
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
touch = TouchSensor(Port.S1)
color = ColorSensor(Port.S3)

wheel_diam=38.1 # in mm
axle_track=114.3 # in mm

robot = DriveBase(left_motor, right_motor, wheel_diam, axle_track)

def check_cancel() -> bool:
    ''' if brick button pressed, return True'''
    global ev3
    button_list = ev3.buttons.pressed()
    if len(button_list) > 0:
        return True
    else:
        return False

def back_up_and_turn(speed:int=100,turn:int=20,distance:int=-50):
    """ 
    Back up the bot to the right when bot sees the black line
    Uses the global vars to access the robot
    """
    global robot
    global ev3
    print("backup!")
    'reset counter so that it starts at 0 and starts counting negative as the bot backs up'
    robot.reset()
    while robot.distance() > distance:
        'drive backward ( this is -speed) and turn to left (-20)'
        robot.drive(-speed, turn)
        print("Backup dist: %f" % (robot.distance()))
        ev3.speaker.beep()
        'pause 100 millisenconds before next check'
        wait(100)
    robot.stop()
    robot.reset()

def drive_forward(speed=100):
    """Drive foward at speed"""
    global robot
    robot.drive(speed, 0)

def is_line():
    '''if line, return True, else False'''
    global color
    if color.color() == Color.BLACK:
        return True
    else:
        return False


if __name__ == "__main__":
    """ 
    While not cancelled by pressing button on brick,
    if on black line, backup to left
    else, 
    if bumped, drive forward fast, 
    else drive forward
    """
    while not check_cancel():
        if is_line():
            'backup steering to the right'
            back_up_and_turn(20)
        elif touch.pressed():
            'drive forward fast!'
            drive_forward(1000)
        else:
            'drive forward normal'
            drive_forward(100)
        wait(100)
