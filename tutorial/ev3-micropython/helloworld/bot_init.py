
"""
The following are the library imports for this program
"""
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
