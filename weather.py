import time
import requests
import json
from datetime import datetime


# Custom location (59.78, 29.95)
API = "c2a531139070ad9d4e372a7448a6732e"
URL = f"https://api.openweathermap.org/data/2.5/weather?lat=59.78&lon=29.95&lang=ru&appid={API}&units=metric"
answer = []

def weather():
    global weather_description
    # s = requests.get(URL).text
    # print(s)
    # with open("wheather.json", "w", encoding="UTF-8") as file:
    #     file.write(s)
    #     print("file write ok")
    # time.sleep(1)
    with open("wheather.json", "r", encoding="utf-8") as file:
        info = json.load(file)

    for i in info["weather"]:
        weather_description = i["description"]

    temperature = info["main"]["temp"]
    temperature_min = info["main"]["temp_min"]
    temperature_max = info["main"]["temp_max"]
    pressure = info["main"]["pressure"]
    humidity = info["main"]["humidity"]
    wind = info["wind"]["speed"]
    clouds = info["clouds"]["all"]
    sunrise = datetime.utcfromtimestamp(info["sys"]["sunrise"]).strftime('%H:%M:%S')
    sunset = datetime.utcfromtimestamp(info["sys"]["sunset"]).strftime('%H:%M:%S')
    return(f"Температура:{temperature} (min {temperature_min}, max {temperature_max}), Давление: {pressure},"
           f" Влажность: {humidity}%, Небо: {weather_description},"
           f" Ветер: {wind}  м/с, Облака: {clouds}%, Восход: {sunrise}, Закат: {sunset}")

print(weather())
