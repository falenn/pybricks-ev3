#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick



# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
ev3 = EV3Brick()

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


# Calculate the light threshold. Choose values based on your measurements.
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 100

# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
PROPORTIONAL_GAIN = 1.2
kp=1.7
ki=0.03
kd=2.0
integral_range=20
integral_rate=10
feed_forward=5

sensor_target=20
max_range=60-sensor_target
steering_proportion=.7
max_steering_angle=120

robot.stop()

robot.heading_control.pid(kp, ki, kd, \
    integral_range, integral_rate, feed_forward)




# Start following the line endlessly.
robot.reset()
while robot.distance() < 1524:
    # Calculate the deviation from the threshold.
    #deviation = line_sensor.reflection() - threshold
    val = line_sensor.reflection() # will be a # between 0 and 60ish
    diff = val - sensor_target
    turn = ((diff/max_range)*max_steering_angle) * -1
    speed = 1000  # maybe make inverse proportional to turn
    #    turn = turn * -1 
    print("Val: %d diff: %f Turn: %f distance: %f" % (val, diff, turn, robot.distance()))

    if val > sensor_target:
        robot.drive(speed, turn)    # turn to the right
    else:
        robot.drive(speed, turn)
    wait(5)