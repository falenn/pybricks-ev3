from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
from time import sleep
import os
import module as modExample
from module import modFunction

# My current path
print(os.path)

# init motor_b
left_motor = Motor(Port.B)
# init motor_c
right_motor = Motor(Port.C)

#reference to the brick
ev3 = EV3Brick()

# https://pybricks.github.io/ev3-micropython/examples/robot_educator_basic.html
robot = DriveBase(left_motor, right_motor, 55.5, 104)

# print using an F-String
print(F"The current state is {robot.state()} with power {ev3.battery}")

# Drive a certain speed - % of 100% power
lspeed = rspeed = 35
left_motor.run(lspeed)
right_motor.run(rspeed)

# wait 2 sec
sleep(2)

# stop motors
right_motor.stop()
left_motor.stop()

# Run motors for 90 degrees - 1/4 rotation of the wheels
left_motor.run_target(lspeed,90)
right_motor.run_target(lspeed,90)


# drive robot using built-in functions
# drive forward a distance in mm
robot.straight(100)

# reset internal measurement to 0
robot.reset()

# drive to a specific distance
while(robot.distance() > 100):
  robot.drive(35,0)

# As this script starts to get messy, we will want to break up our functionality.
# One way to do this is through modules - functions in scripts (other files) in the
# same directory as this script.
modExample.modFunction("Imported module module.py")

# Here, we called the modExample.modFunction() from the module.py file in this
# same directory.  The import above:
# import module as modExample, imports the module and gives it an alias.

# We could also import just the needed function from the module
modFunction("Just the function")
