#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from umqtt.robust import MQTTClient



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
wheel_diameter = 41.25
axle_base = 104
mqtt_broker = "172.16.0.41"
bot_id = "ev3dev_bot6"
topic_wind = "weather/windDirection"
topic_temp = "weather/temperature"
topic_condition = "weather/condition"
topic_status = "status/bots"
topic_bot_cs_status = "status/bots/" + bot_id + "/sensors/color"
topic_bot_lm_status = "status/bots/" + bot_id + "/motors/left"
topic_bot_rm_status = "status/bots/" + bot_id + "/motors/right"


last_angle = 0

# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
cs = ColorSensor(Port.S3)
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_base)

def getdata(topic, msg):
    ev3.screen.clear()
    print("topic: %s: %s" % (topic, str(msg.decode('utf-8'))))
    if topic == b'weather/temperature':
        sound_temp(int(float(msg)))

    if topic == b'weather/windDirection':
        turn_to_wind(int(float(msg)))

    if topic == b'weather/condition':
        show_condition(str(msg))
    
    


# rotate into the wind
'''
if degrees = 315.0, turn the bot to face 315.  Starting heading is 0 - North.
'''
def turn_to_wind(degrees=0):
    print("turn_to_wind")
    global last_angle
    angle_to_turn = 0
    angle_to_turn = int(degrees - last_angle)
    print("angle_to_turn: %d = %d - %d" % (angle_to_turn, degrees, last_angle))
    ev3.screen.print("wind dir: %d turn: %d" % (degrees, angle_to_turn))
    last_angle = degrees
    print("last_angle: %d"% (last_angle))
    robot.turn(angle_to_turn)

def sound_temp(temperature=20):
    print("sound_temp %d" % temperature)
    temp = temperature + 500
    ev3.speaker.beep(temp, duration=100)
    temp_in_f = int(temperature * 1.8 + 32)
    ev3.screen.print("temp: %d c" % (temp_in_f))

def show_condition(condition="none"):
    ev3.screen.print(condition)

def mqtt_status():
    client.publish(topic_status, bot_id + " connected")
    
def mqtt_disconnect():
    client.publish(topic_status, bot_id + " disconnected")
    client.disconnect()

def bot_status():
    client.publish(topic_bot_cs_status, str(cs.reflection()))
    #client.publish(topic_bot_lm_status, str(left_motor.angle()))
    #client.publish(topic_bot_rm_status, str(right_motor.angle()))
    

if __name__ == "__main__":
    ev3.speaker.beep()
    try:
        # Create MQTT client
        client = MQTTClient(bot_id, mqtt_broker)
        client.set_callback(getdata)
        client.connect()
        mqtt_status()
        client.subscribe(topic_wind)
        client.subscribe(topic_temp)
        client.subscribe(topic_condition)
        
        while True:
            client.check_msg()
            bot_status()
            wait(1000)
        
    except Exception as e:
        print("Error: %s" % (e))
        mqtt_disconnect()