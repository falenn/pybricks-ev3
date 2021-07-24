#!/usr/bin/env python
import requests
from requests.exceptions import HTTPError
import json

apikey = 'YOUR_API_KEY'

URL = 'https://api.tomorrow.io/v4/'
API_KEY_HEADER='apikey'
API_KEY='jBjFa4Bh506aaPfnHwkL39c0O4OeAmlw'
ANNAP_LAT=38.978443
ANNAP_LON=-76.492180
headers = {"Accept":"application/json","apikey":API_KEY}


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


# retrieve weather using locationID
def get_weather(location_id):
    print(f"get weather")
    querystring = {"units":"metric","timesteps":"1h","location":location_id,"fields":['windDirection']}
    response = requests.request("GET",URL+"timelines", headers=headers, params=querystring)
    return response.text

if __name__ == "__main__":
    print(f"Begin main")
    id = get_location("Annapolis")

    weather = get_weather(id)
    print(f"Weather: " + weather)