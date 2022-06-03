import requests
import os
from pprint import pprint

def get_coord_weather(lat,lon,appid):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}")
    return pprint(response.json()["weather"])

get_coord_weather(os.environ.get('LAT'), os.environ.get('LONG'), os.environ.get('API_KEY'))