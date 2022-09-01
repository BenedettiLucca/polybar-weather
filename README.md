# polybar-weather
Display weather status in polybar.

### Dependecies
- Python3
- Nerd Fonts

### Settings
Add the following to .../polybar/modules:
``` ini
[module/weather]
type = custom/script
exec = python ~/path/to/polybarWeather.py -i 745042 -a appid123goes456here789 -t Celcius
```
And edit the path to weatherIcons.json in polybarWeather.py
``` ini
with open('your_location/weatherIcons.json') as file:
    d = json.loads(file.read())
```

### Usage
Here is the parameters.

-i CityId
-a AppID
-t OutputType
-z ZipCode
-c CountryCode

### Getting Started
First of all, Application ID is needed;
You can get your individual AppID by signing up to openweathermap and going to the API section:
https://home.openweathermap.org/users/sign_up

#### Getting Status
There are two ways to get weather status: using cityID or using both ZipCode and CountryCode. ApplicationID is needed for each way.
Here is example for each ways:
``` ini
python ~/path/to/polybarWeather.py -i 745042 -a appid123goes456here789
```
In the example above, 745042 is the city id of Istanbul, below there is an information on getting your city's id. And the output will be:
```
 8°C
```
Celcius is the default output type, you can change it to Fahrenheit or Kelvin.
``` ini
python ~/path/to/polybarWeather.py -z 34704 -c tr -a appid123goes456here789 -t Fahrenheit
```
##### Finding City ID
Information on supported cities are given in a json format with the name 'city.list.json.gz' and can be downloaded from:
http://bulk.openweathermap.org/sample/
