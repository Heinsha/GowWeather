# IMPORTS ____________________________________________________
from urllib.request import Request, urlopen
import json
from graphics import GraphWin, Text, Point
import time
import textwrap

# API CALLER _________________________________________________
API_KEY = 'c41b99facc8c41aa'
url = 'http://api.wunderground.com/api/{}/geolookup/conditions/forecast/q/NY/pws:KNYSOUTH27.json'.format(API_KEY)

# DATA RETRIEVE ______________________________________________
request = Request(url)
response = urlopen(request)
json_string = response.read().decode('utf8')
parsed_json = json.loads(json_string)

###
locationSource = parsed_json['current_observation']['observation_location']['full']
humiditySource = parsed_json['current_observation']['relative_humidity']
weatherSource = parsed_json['current_observation']['weather']
temp_f = parsed_json['current_observation']['temp_f']
feelslike_f = parsed_json['current_observation']['feelslike_f']
temp_c = parsed_json['current_observation']['temp_c']
feelslike_c = parsed_json['current_observation']['feelslike_c']

###
fc1Chk = parsed_json['forecast']['txt_forecast']['forecastday'][0]['title']
fc1Src = parsed_json['forecast']['txt_forecast']['forecastday'][0]['fcttext']
fc2Src = parsed_json['forecast']['txt_forecast']['forecastday'][1]['fcttext']
fc3Src = parsed_json['forecast']['txt_forecast']['forecastday'][2]['fcttext']
fc4Src = parsed_json['forecast']['txt_forecast']['forecastday'][3]['fcttext']
fc5Src = parsed_json['forecast']['txt_forecast']['forecastday'][4]['fcttext']
timeNow = float(time.strftime('%H%M%S'))

# UI CURRENT WEATHER __________________________________________
win = GraphWin('Gow Weather', 1000, 300)
location = Text(Point(500, 20), locationSource)
temp = Text(Point(500, 60), "Temperature:   " + str(temp_f) + "Fº   /   " + str(temp_c) + "Cº")
temp2 = Text(Point(500, 80), "Feels like:        " + str(feelslike_f) + "Fº   /   " + str(feelslike_c) + "Cº")
weather = Text(Point(500, 100), "Current conditions:   " + str(weatherSource))
humidity = Text(Point(500, 120), "Humidity:   " + str(humiditySource))

# UI FORECAST _________________________________________________
forecast = Text(Point(500, 160), "Forecast:")
sep = Text(Point(500, 163), "_____________________________________________________________")

# IF STATEMENTS _______________________________________________
if fc1Chk is "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday" or "Saturday" or "Sunday":
        forecast1str = "Today:     " + textwrap.fill(fc1Src,120)
        forecast2str = "Tonight:     " + textwrap.fill(fc2Src,120)
        forecast3str = "Tomorrow:     " + textwrap.fill(fc3Src,120)
else:
        forecast1str = "Tonight:     " + textwrap.fill(fc1Src,120)
        forecast2str = "Tomorrow:     " + textwrap.fill(fc2Src,120)
        forecast3str = "Tomorrow Night:     " + textwrap.fill(fc3Src,120)
###
if len(forecast1str) > 120:
        offset1 = 195
else:
        offset1 = 185
###
if len(forecast2str) > 120:
        offset2 = 215
elif len(forecast2str) > 120 and offset1 is 195:
                offset2 = 225
else:
        offset2 = 205
###
if len(forecast3str) > 120:
        offset3 = 235
elif len(forecast3str) > 120 and offset2 is 215:
                offset3 = 245
elif len(forecast3str) > 120 and offset2 is 225:
                offset3 = 255
else:
        offset3 = 225

#______________________________________________________________
forecast1 = Text(Point(500, offset1), forecast1str)
forecast2 = Text(Point(500, offset2), forecast2str)
forecast3 = Text(Point(500, offset3), forecast3str)

# DRAW ________________________________________________________
location.draw(win)
temp.draw(win)
temp2.draw(win)
weather.draw(win)
humidity.draw(win)
forecast.draw(win)
sep.draw(win)
forecast1.draw(win)
forecast2.draw(win)
forecast3.draw(win)
