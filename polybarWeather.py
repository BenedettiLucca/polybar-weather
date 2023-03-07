import requests
import json
import urllib.parse

def getWeatherByLatLon(lat, lon):
    url = 'https://weather.contrateumdev.com.br/api/weather?lat=' + str(lat) + '&lon=' + str(lon)
    r = requests.get(url)
    try:
        return r.json()
    except ValueError:
        return {}

def getWeatherByCityState(city, state):
    url = 'https://weather.contrateumdev.com.br/api/weather/city/?city=' + city + ',' + state
    r = requests.get(url)
    try:
        return r.json()
    except ValueError:
        return {} 

method = 'lat/lon' # change to city/state if you want to use it this way

if method == 'lat/lon':
    with open('path of config.json') as file:
        config = json.loads(file.read())
    latitude = config["lat"]
    longitude = config["lon"]
    r = getWeatherByLatLon(latitude, longitude)
elif method == 'city/state':
    with open('path of config.json') as file:
        config = json.loads(file.read())
    city = urllib.parse.quote(config["city"])
    state = urllib.parse.quote(config["state"])
    r = getWeatherByCityState(city, state)
else:
    print('invalid method')

with open('path of weatherIcons.json') as file:
    d = json.loads(file.read())

if not r:
    print("")
else:
    temp = int(r["main"]["temp"])
    weather = r['weather'][0]['icon']
    weatherIcon = d[f'{weather}']
    print(weatherIcon + ' ' + str(temp) + '°C')
