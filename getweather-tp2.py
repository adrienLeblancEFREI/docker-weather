import requests
import os
from pprint import pprint
from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods =['GET'])
def get_coord_weather():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    appid = str(os.environ.get('API_KEY'))
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}")
    return str(response.json())

if __name__ == "__main__":
    app.run(port = 8081,debug=True)
    get_coord_weather()