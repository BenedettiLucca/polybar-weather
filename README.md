# polybar-weather
Display weather status in polybar.

### Dependecies
- Python3
- Nerdfonts
### Settings
Add the following to .../polybar/modules
``` ini
[module/weather]
type = custom/script
exec = python ~/path/to/polybarWeather.py
```
And edit the paths to the json files in polybarWeather.py
``` ini
if method == 'lat/lon':
    with open('your_path/config.json') as file:
        config = json.loads(file.read())
    latitude = config["lat"]
    longitude = config["lon"]
    r = getWeatherByLatLon(latitude, longitude)
elif method == 'city/state':
    with open('your_path/config.json') as file:
        config = json.loads(file.read())
    city = urllib.parse.quote(config["city"])
    state = urllib.parse.quote(config["state"])
    r = getWeatherByCityState(city, state)
else:
    print('invalid method')

with open('your_path/weatherIcons.json') as file:
    d = json.loads(file.read())
```

### Usage
Change parameters in config.json
``` ini
{"lon": -46.6418, "lat": -23.5587, "city": "Sao Paulo", "state": "sao paulo"}
```

### API
I've changed the API from openweather to https://documenter.getpostman.com/view/11074732/TzJpizur
due to request limits. 
