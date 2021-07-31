#!/usr/bin/env python
import requests
from requests.exceptions import HTTPError
import json
import paho.mqtt.client as mqtt
import time
import os
import socket

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

apikey = 'YOUR_API_KEY'

URL = 'https://api.tomorrow.io/v4/'
API_KEY_HEADER='apikey'
API_KEY=os.environ['TOMORROW_API_KEY']
headers = {"Accept":"application/json","apikey":API_KEY}
MQTT_SERVER=IP
fields=['windDirection','temperature','windSpeed','weatherCode']
# timesteps - 1d, 1h, 30m, 15m, 5m, 1m, current
# shorter steps, less data
timestep="1h"


# get all of the locations registered on tomorrow.io
def get_locations():
    try: 
        print(f"get locatons")
        response = requests.request("GET",URL+"locations", headers=headers)
        json_data = json.loads(response.text)
        print(f"data: {json_data}")

        count = len(json_data["data"]["locations"])
        print(f"There are {count} locations")
        return json_data["data"]["locations"]
    except HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")
    except Exception as err:
        print(f"HTTP error occured: {err}")


# get location id for a single location
def get_location(name):
    locations = get_locations()
    id = ""
    for loc in locations:
        print(f"loc id: {loc['id']}, loc name: {loc['name']}")
        if loc['name'].find(name) != -1:
            id = loc['id']
            print("found!")
            break
    print(f"id for location{name}: {id}")
    return id


# retrieve weather using locationID, returns data in a python dict (converting from json)
def get_weather(fields, location="Annapolis", timestep="1h"):
    print(f"get weather {location}")
    location_id = get_location(location)
    querystring = {"units":"metric","timesteps":timestep,"location":location_id,"fields":fields}
    response = requests.request("GET",URL+"timelines", headers=headers, params=querystring)
    return json.loads(response.text)

# for each weather data item, publish to a topic under the topic root
def publish_weather_timeline_sim(mqtt_client, data, topic_root="weather", delay=10):
    print(f"sim: {data}")
    for timeline in data["data"]["timelines"]:
        for interval in timeline["intervals"]:
            print(f"{interval['startTime']}")
            for (key,value) in interval["values"].items():
                #print(f"key: {k}, value:{v}")
                topic = topic_root + "/" + key
                # convert float to string and send
                mqtt_client.publish(topic,payload=str(value))
            time.sleep(delay)

                
def on_message(client, userdata, message):
    topic = message.topic   
    if topic == "weather/weatherCode":
        data = float(message.payload.decode('utf-8'))
        print_weather(data)

    if topic == "status/bots":
        data = message.payload.decode('utf-8')
        print(f"bot {data}")
    
    if topic == "status/bots/ev3dev_bot6/sensors/color":
        data = message.payload.decode('utf-8')
        print(f"{topic}: {data}")
    
    if topic == "status/bots/ev3dev_bot6/motors/left":
        data = message.payload.decode('utf-8')
        print(f"{topic}: {data}")

    if topic == "status/bots/ev3dev_bot6/motors/right":
        data = message.payload.decode('utf-8')
        print(f"{topic}: {data}")

    if topic == "alarm":
        data = message.payload.decode('utf-8')
        print(f"{topic}: {data}")

def print_weather(data=1000):
    data = int(data)
    weather = "clear"
    if data == 1000:
        weather = "clear"
    if data == 1001:
        weather = "cloudy"
    if data == 1100: 
        weather = "Mostly Clear"
    if data == 1101:
        weather = "Partly Cloudy"
    if data == 1102:
        weather = "Mostly Cloudy"
    if data == 2000:
        weather = "Fog"
    if data == 2100:
        weather = "Light Fog"
    if data == 3000:
        weather =  "Light Wind"
    if data == 3001:
        weather =  "Wind"
    if data == 3002:
        weather =  "Strong Wind"
    if data == 4000:
        weather = "Drizzle"
    if data == 4001:
        weather = "Rain"
    if data == 4200:
        weather = "Light Rain"
    if data == 4201:
        weather = "Heavy Rain"
    print(weather)
    client.publish("weather/condition", payload=weather)


if __name__ == "__main__":
    #print(f"Begin main")
    
    
    #Connect to broker
    client = mqtt.Client("rbdge-robotics-weather")
    client.connect(host="172.16.0.41")
    #client.username_pw_set(username="robots",password="robots")

    print(f"clientId:{client._client_id}")
    try:
        #client.connect(host="test.mosquitto.org")
        client.on_message=on_message
        client.subscribe("status/bots")
        client.subscribe("weather/windDirection")
        client.subscribe("weather/temperature")
        client.subscribe("weather/windSpeed")
        client.subscribe("weather/weatherCode")
        client.subscribe("status/bots/ev3dev_bot6/sensors/color")
        client.subscribe("status/bots/ev3dev_bot6/motors/left")
        client.subscribe("status/bots/ev3dev_bot6/motors/right")
        client.subscribe("alarm")
        client.loop_start() #start the loop

        # now, get weather data and publish every 10 sec
        weather = get_weather(fields=fields, location="Annapolis", timestep=timestep)
        publish_weather_timeline_sim(mqtt_client=client, data=weather, topic_root="weather", delay=10)
        
        
        time.sleep(60)
        client.loop_stop()
        #else:
            #print(f"Not Connected [{client._host}:{client._port}::{client._protocol}]")
    except Exception as err:
        print(f"mqtt client error occured: {err}")
    #client.disconnect()