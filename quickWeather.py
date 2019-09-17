# quickWeather.py - Prints the weather for a location from the command line.

import json
import requests
import sys

send_url= 'http://ip-api.com/json/'
r= requests.get(send_url)
j= json.loads(r.text)
location= j['city']
lat= j['lat']
lon= j['lon']

print("\nGeo Location: ",lat, ',', lon, '\n')

# Download the JSON data from Accuweather's API.
url ='http://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&APPID=7f68cf5407d5bcc5704df85b1852f54c&units=imperial' % (lat,lon)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.
w = weatherData['list']

print("Current weather in %s:" % (location), '\n**********************************************\n')

for i in range(0,3):
    print("Day %s" % (i+1))
    print(w[i]['weather'][0]['main'], '               ', w[i]['weather'][0]['description'])
    print("Temperature           ", w[i]['main']['temp'],'°F')
    print("Min Temperature       ", w[i]['main']['temp_min'],'°F')
    print("Max Temperature       ", w[i]['main']['temp_max'],'°F')
    print("Humidity              ", w[i]['main']['humidity'])
    print()