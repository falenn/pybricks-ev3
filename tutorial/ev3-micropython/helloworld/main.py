#!/usr/bin/env pybricks-micropython
"""
#!/usr/bin/env pybricks-micropython - this is the way we specifiy the binary executable for this file
pybricks-micropython executes on the robot.
"""

"""
The following are the library imports for this program
"""
from time import sleep
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop


"""
Here we init the program with global variables defining the robot
"""
# Create objects here
ev3 = EV3Brick()
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)

def e5():
    return 659.25

def d5():
    return 587.33

def c5():
    return 523.25

def turn_left_half_way(speed=500):
    global right_motor
    right_motor.run_target(speed, 978, then=Stop.BRAKE, wait=True)
    sleep(1)

def turn_right_half_way(speed=500):
    global left_motor
    left_motor.run_target(speed, 978, then=Stop.BRAKE, wait=True)
    sleep(1)
    

if __name__ == "__main__":
    ev3.speaker.beep(e5(),1000)
    ev3.speaker.beep(d5(),1000)
    ev3.speaker.beep(c5(),1000)
    print("Hello world!")
    
    turn_left_half_way()
    turn_right_half_way()
    turn_left_half_way()
    turn_right_half_way()
    turn_left_half_way()
    turn_right_half_way()

    sleep(20)
    ev3.speaker.beep(c5(),1000)

    