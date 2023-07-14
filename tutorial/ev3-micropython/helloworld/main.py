#!/usr/bin/env pybricks-micropython
"""
#!/usr/bin/env pybricks-micropython - this is the way we specifiy the binary executable for this file
pybricks-micropython executes on the robot.
"""

"""
The following are the library imports for this program
"""
from time import sleep
from bot_init import ev3, right_motor, left_motor
from pybricks.parameters import Port, Stop
from music import Music

"""
Functions for use in the program
"""
def turn_left_half_way(speed:int=500):
    """
    Using only the right motor, turn to the left slightly and brake.  Do not continue until this is done.
    Use the speed supplied with a default of 500.
    Sleep 1 second.
    """
    global right_motor
    right_motor.run_target(speed, 978, then=Stop.BRAKE, wait=True)
    sleep(1)

def turn_right_half_way(speed:int=500):
    """
    Using only the left motor, turn to the right slightly and brake.  Do not continue until this is done.
    Use the speed supplied with a default of 500.
    Sleep 1 second.
    """
    global left_motor
    left_motor.run_target(speed, 978, then=Stop.BRAKE, wait=True)
    sleep(1)
    
"""The MAIN Program"""
if __name__ == "__main__":
    """Playing music using our class Music as a namespace for our tone constants"""
    ev3.speaker.beep(Music.E5,500)
    ev3.speaker.beep(Music.D5,500)
    ev3.speaker.beep(Music.C5,500)
    sleep(.5)
    ev3.speaker.beep(Music.E5,500)
    ev3.speaker.beep(Music.D5,500)
    ev3.speaker.beep(Music.C5,500)
    sleep(.5)
    ev3.speaker.beep(Music.C5,200)
    sleep(.050)
    ev3.speaker.beep(Music.C5,200)
    sleep(.050)
    ev3.speaker.beep(Music.C5,200)
    sleep(.050)
    ev3.speaker.beep(Music.C5,200)
    sleep(.050)
    ev3.speaker.beep(Music.D5,200)
    sleep(.050)
    ev3.speaker.beep(Music.D5,200)
    sleep(.050)
    ev3.speaker.beep(Music.D5,200)
    sleep(.050)
    ev3.speaker.beep(Music.D5,200)
    sleep(.050)
    ev3.speaker.beep(Music.E5,500)
    ev3.speaker.beep(Music.D5,500)
    ev3.speaker.beep(Music.C5,500)


    'Print the coloquial hello world statement for a first time program'
    print("Hello world!")
    
    'make some robot turns'
    turn_left_half_way()
    turn_right_half_way()
    turn_left_half_way()
    turn_right_half_way()
    turn_left_half_way()
    turn_right_half_way()

    'go to sleep'
    sleep(1)

    'make some noise!'
    ev3.speaker.beep(Music.C5,1000)

    'end of the program.'