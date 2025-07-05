# CLI WEATHER VISUALZIER 
# USING WTTR.IN

import requests
import matplotlib.pyplot as plt
import json
import utils

# for requests and json
url = "https://wttr.in/London?format=j1"
res = requests.get(url)
data = res.json()


# for easy access
country = data['nearest_area'][0]['country'][0]['value']
city = data['nearest_area'][0]['areaName'][0]['value']
date = data['weather'][0]['date']


# get hourly temperatures for today
today = data['weather'][0]['hourly']
rain = [] # chance of rain; will average this
time = []
temp = []
for hour in today:
    time.append(hour['time'])
    temp.append(int(hour['tempC']))
    rain.append(int(hour['chanceofrain']))
    #print(f"Time: {time} | Temp: {temp}\u00B0C")


# average the chance of rain
avg_rain = round(sum(rain) / len(rain), 0)


# data for today
utils.display("WEATHER VISUALIZER")
print(f"Location: {country}, {city}")
print(f"Observation time: {data['current_condition'][0]['localObsDateTime']}")
print(f"Description: {data['current_condition'][0]['weatherDesc'][0]['value']}")
print(f"Temperature: {data['current_condition'][0]['temp_C']}\u00B0C")
print(f"Feels like: {data['current_condition'][0]['FeelsLikeC']}\u00B0C")
print(f"Humidity: {data['current_condition'][0]['humidity']}")
print(f"Chance of rain: {avg_rain}%")
print(f"Wind speed: {data['current_condition'][0]['windspeedKmph']} kph")
print(f"Sunrise: {data['weather'][0]['astronomy'][0]['sunrise']}")
print(f"Sunset: {data['weather'][0]['astronomy'][0]['sunset']}")
utils.hyphens()


# graph the hourly temperatures for today
plt.title(f"Hourly Weather Forecast for {city} ({date})")
plt.xlabel("Time (hours)")
plt.ylabel("Temp (\u00B0C)")
plt.plot(time, temp)
plt.show()
plt.close()


