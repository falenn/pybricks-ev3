from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
ev3 = EV3Brick()

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)

wheel_diam=38.1
axle_track=114.3

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, \
    wheel_diameter=wheel_diam, axle_track=axle_track)

# Calculate the light threshold. Choose values based on your measurements.
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

# anything less than threshold is the line
threshold = 20

# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 100
PROPORTIONAL_GAIN = 1.2

def check_cancel():
    ''' if brick button pressed, return True'''
    global ev3
    button_list = ev3.buttons.pressed()
    if len(button_list) > 0:
        return True
    else:
        return False

def say_something(phrase=""):
    global ev3
    ev3.speaker.set_volume(100)
    ev3.speaker.set_speech_options(voice=f1)
    ev3.speaker.say(phrase)


if __name__ == "__main__":
    
    say_something("Robotics is great")

    while not check_cancel():

        #if line_sensor.reflection() > threshold:
            # line_sensor sees white  - not on the line
        #    robot.drive(DRIVE_SPEED, 20)
        #else:
            # turn away from the line
        #    robot.drive(DRIVE_SPEED, -20)
        #wait(10)

        deviation = line_sensor.reflection() - threshold
        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation
        # Set the drive base speed and turn rate.
        speed = DRIVE_SPEED
        if turn_rate > 0:
            speed = max(DRIVE_SPEED/(turn_rate/2), 60)
        robot.drive(speed, turn_rate)
        # You can wait for a short time or do other things in this loop.
        wait(10)


# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
PROPORTIONAL_GAIN = 1.2

# Start following the line endlessly.
while True:
    # Calculate the deviation from the threshold.
    deviation = line_sensor.reflection() - threshold

    # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation

    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)

    # You can wait for a short time or do other things in this loop.
    wait(10)