# IMPORTS
from urllib.request import Request, urlopen
import json
from graphics import GraphWin, Text, Point
import time
import textwrap

# API CALLER
API_KEY = 'c41b99facc8c41aa'
url = 'http://api.wunderground.com/api/{}/geolookup/conditions/forecast10day/q/NY/pws:KNYSOUTH27.json'.format(API_KEY)

# DATA RETRIEVE
request = Request(url)
response = urlopen(request)
json_string = response.read().decode('utf8')
parsed_json = json.loads(json_string)

locationSource = parsed_json['current_observation']['observation_location']['full']
humiditySource = parsed_json['current_observation']['relative_humidity']
weatherSource = parsed_json['current_observation']['weather']
temp_f = parsed_json['current_observation']['temp_f']
feelslike_f = parsed_json['current_observation']['feelslike_f']
temp_c = parsed_json['current_observation']['temp_c']
feelslike_c = parsed_json['current_observation']['feelslike_c']

fc1Src = parsed_json['forecast']['txt_forecast']['forecastday'][0]['fcttext']
fc2Src = parsed_json['forecast']['txt_forecast']['forecastday'][1]['fcttext']
fc3Src = parsed_json['forecast']['txt_forecast']['forecastday'][2]['fcttext']
timeNow = float(time.strftime('%H%M%S'))

# UI
win = GraphWin('Gow Weather', 1000, 300)
location = Text(Point(500, 20), locationSource)
temp = Text(Point(500, 60), "Temperature:   " + str(temp_f) + "Fº   /   " + str(temp_c) + "Cº")
temp2 = Text(Point(500, 80), "Feels like:        " + str(feelslike_f) + "Fº   /   " + str(feelslike_c) + "Cº")
weather = Text(Point(500, 100), "Current conditions:   " + str(weatherSource))
humidity = Text(Point(500, 120), "Humidity:   " + str(humiditySource))
forecast = Text(Point(500, 160), "Forecast:")
sep = Text(Point(500, 163), "_____________________________________________________________")
forecastToday = Text(Point(500, 185), "Today:   " + textwrap.fill(fc1Src,120))
forecastTonight1 = Text(Point(500, 185), "Tonight:   " + textwrap.fill(fc2Src,120))
forecastTonight2 = Text(Point(500, 205), "Tonight:   " + textwrap.fill(fc2Src,120))
forecastTomorrow = Text(Point(500, 205), "Tomorrow:   " + textwrap.fill(fc3Src,120))
forecastTodayLong = Text(Point(500, 205), "Today:   " + textwrap.fill(fc1Src,120))
forecastTonight1Long = Text(Point(500, 205), "Tonight:   " + textwrap.fill(fc2Src,120))
forecastTonight2Long = Text(Point(500, 245), "Tonight:   " + textwrap.fill(fc2Src,120))
forecastTomorrowLong = Text(Point(500, 245), "Tomorrow:   " + textwrap.fill(fc3Src,120))

    # UI - IF STATEMENT
if timeNow < 180000:
    if len(str(forecastToday)) > 120 and len(str(forecastTonight2)) > 120:
        forecastTodayLong.draw(win)
        forecastTonight2Long.draw(win)
    elif len(str(forecastToday)) > 120:
        forecastTodayLong.draw(win)
        forecastTonight2.draw(win)
    elif len(str(forecastTonight2)) > 120:
        forecastToday.draw(win)
        forecastTonight2Long.draw(win)
    else:
        forecastToday.draw(win)
        forecastTonight2.draw(win)
else:
    if len(str(forecastTonight1)) > 120 and len(str(forecastTomorrow)) > 120:
        forecastTonight1Long.draw(win)
        forecastTomorrowLong.draw(win)
    elif len(str(forecastTonight1)) > 120:
        forecastTonight1Long.draw(win)
        forecastTomorrow.draw(win)
    elif len(str(forecastTomorrow)) > 120:
        forecastTonight1.draw(win)
        forecastTomorrowLong.draw(win)
    else:
        forecastTonight1.draw(win)
        forecastTomorrow.draw(win)

# DRAW
location.draw(win)
temp.draw(win)
temp2.draw(win)
weather.draw(win)
humidity.draw(win)
forecast.draw(win)
sep.draw(win)
