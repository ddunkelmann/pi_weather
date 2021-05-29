#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 12:17:28 2021

@author: hhemba334
"""

from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk

# API Key: ab0ec2b1147266a1e70f838a21f450b8
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

import json
import requests
import time

location = "Ohlsdorf"
Response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ location + "&APPID=ab0ec2b1147266a1e70f838a21f450b8")

WeatherData = Response.json()


root = Tk()

root.title = "Weather Dashboard"
root.geometry = "900x900"
root.config(background = "#4d4d4d")



Grid.columnconfigure(root, 0, weight = 1)
Grid.rowconfigure(root, 0, weight = 1)
Grid.rowconfigure(root, 1, weight = 5)

grid_pad = 2

# Frame: Basic Infos --------------- #
frame_basic = Frame(root, padx = grid_pad, pady = grid_pad, background = "#4d4d4d")
frame_basic.grid(row = 0, column = 0, sticky = "NSWE")

Grid.columnconfigure(frame_basic, 0, weight = 1)
Grid.columnconfigure(frame_basic, 1, weight = 1)
Grid.columnconfigure(frame_basic, 2, weight = 1)
Grid.rowconfigure(frame_basic, 0, weight = 1)


# - Datumsangabe + Zeit 
now = datetime.now()

date_label = Label(frame_basic, text = datetime.fromtimestamp(WeatherData["dt"]).strftime('%d.%m.%Y'), font = ("Open Sans", 20), bg = "#2b2b2b", fg = "white")
date_label.grid(row = 0, column = 0, sticky = "NSWE", padx = grid_pad, pady = grid_pad)

time_label = Label(frame_basic, text = datetime.fromtimestamp(WeatherData["dt"]).strftime("%H:%M:%S"), font = ("Open Sans", 20), bg = "#2b2b2b", fg = "white")
time_label.grid(row = 0, column = 1, sticky = "NSWE", padx = grid_pad, pady = grid_pad)

place_label = Label(frame_basic, text = location, font = ("Open Sans", 20), bg = "#2b2b2b", fg = "white")
place_label.grid(row = 0, column = 2, sticky = "NSWE", padx = grid_pad, pady = grid_pad)



# ---------------------------------- # 



# Temperatur Frame ----------------- # 
frame_temp = Frame(root, padx = grid_pad, pady = grid_pad, background = "#4d4d4d")
frame_temp.grid(row = 1, column = 0, sticky = "NSWE")

Grid.columnconfigure(frame_temp, 0, weight = 1)
Grid.columnconfigure(frame_temp, 1, weight = 1)
Grid.columnconfigure(frame_temp, 2, weight = 1)
Grid.rowconfigure(frame_temp, 0, weight = 1)
Grid.rowconfigure(frame_temp, 1, weight = 1)
Grid.rowconfigure(frame_temp, 2, weight = 1)

# - Temperatur in C
temperatur = Label(frame_temp, text = "{}°C".format(round(WeatherData["main"]["temp"] - 273, 1)), font = ("Open Sans", 80), bg = "#2b2b2b", fg = "white")
temperatur.grid(row = 0, column = 0, rowspan = 3, sticky = "NSWE", padx = grid_pad, pady = grid_pad)

# - Bild zur Temperatur

main_weather = WeatherData["weather"][0]["main"]

if main_weather in ["Mist", "Fog", "Haze", "Smoke", "Dust", "Ash", "Squall", "Tornado", "Sand"]:
    main_weather = "Mist"

# Nur Testing
# main_weather = "Thunderstorm"


resize_factor = 1.5

weather_image = Image.open(f"/Users/hhemba334/Documents/Programmieren/GIT/python/rasp_weatherApp/IMG/{main_weather}.png")
weather_resize = weather_image.resize((round(weather_image.size[0] / resize_factor), round(weather_image.size[1] / resize_factor)))
weather_img = ImageTk.PhotoImage(weather_resize)

temp_img = Label(frame_temp, image = weather_img, bg = "#2b2b2b")
temp_img.grid(row = 0, column = 1, rowspan = 3, sticky = "NSWE", padx = grid_pad, pady = grid_pad)

# - Gefühlte Temperatur
temp_feel = Label(frame_temp, text = "Gefühlt: {}°C".format(round(WeatherData["main"]["feels_like"] - 273, 1)), font = ("Open Sans", 25), bg = "#2b2b2b", fg = "white")
temp_feel.grid(row = 0, column = 2, sticky = "NSWE", padx = grid_pad, pady = grid_pad)

# - Luftdruck
pressure = Label(frame_temp, text = "Luftdruck: {} hPa".format(WeatherData["main"]["pressure"]), font = ("Open Sans", 25), bg = "#2b2b2b", fg = "white")
pressure.grid(row = 1, column = 2, sticky = "NSWE", padx = grid_pad, pady = grid_pad)

# - Luftfeuchtigkeit
humid = Label(frame_temp, text = "Luftfeuchtigkeit: {}%".format(WeatherData["main"]["humidity"]), font = ("Open Sans", 25), bg = "#2b2b2b", fg = "white")
humid.grid(row = 2, column = 2, sticky = "NSWE", padx = grid_pad, pady = grid_pad)

# ---------------------------------- # 




# Sonnenaufgang und -Untergang Frame ----------------- # 
frame_sun = Frame(root, padx = grid_pad, pady = grid_pad, background = "#2b2b2b")
frame_sun.grid(row = 2, column = 0,  padx = grid_pad + 2, pady = grid_pad + 2, sticky = "nsew")


Grid.columnconfigure(frame_sun, 0, weight = 1)
Grid.columnconfigure(frame_sun, 1, weight = 1)
Grid.columnconfigure(frame_sun, 2, weight = 1)
Grid.columnconfigure(frame_sun, 3, weight = 1)
Grid.rowconfigure(frame_sun, 0, weight = 1)
Grid.rowconfigure(frame_sun, 1, weight = 1)

header_size = 22
time_size = 18
resize_factor_sun = 3


# - Bild Sonnenaufgang
sunrise_image = Image.open("/Users/hhemba334/Documents/Programmieren/GIT/python/rasp_weatherApp/IMG/sunrise.png")
sunrise_resize = sunrise_image.resize((round(sunrise_image.size[0] / resize_factor_sun), round(sunrise_image.size[1] / resize_factor_sun)))
sunrise_img = ImageTk.PhotoImage(sunrise_resize)
sunrise_picture = Label(frame_sun, image = sunrise_img, bg = "#2b2b2b")
sunrise_picture.grid(row = 0, column = 0, rowspan = 2, sticky = "E")

# - Zeit Sonnenaufgang
sunrise = Label(frame_sun, text = "Sonnenaufgang:", font = ("Open Sans", header_size), bg = "#2b2b2b", fg = "white")
sunrise.grid(row = 0, column = 1, padx = 20, sticky = "W")
sunrise_time = Label(frame_sun, text = datetime.fromtimestamp(WeatherData["sys"]["sunrise"]).strftime("%H:%M:%S"), font = ("Open Sans", time_size), bg = "#2b2b2b", fg = "white")
sunrise_time.grid(row = 1, column = 1, padx = 20, sticky = "W")




# - Bild Sonnenuntergang
sunset_image = Image.open("/Users/hhemba334/Documents/Programmieren/GIT/python/rasp_weatherApp/IMG/sunset.png")
sunset_resize = sunset_image.resize((round(sunset_image.size[0] / resize_factor_sun), round(sunset_image.size[1] / resize_factor_sun)))
sunset_img = ImageTk.PhotoImage(sunset_resize)
sunset_picture = Label(frame_sun, image = sunset_img, bg = "#2b2b2b")
sunset_picture.grid(row = 0, column = 2, rowspan = 2, sticky = "E")

# - Zeit Sonnenuntergang
sunset = Label(frame_sun, text = "Sonnenuntergang:", font = ("Open Sans", header_size), bg = "#2b2b2b", fg = "white")
sunset.grid(row = 0, column = 3, padx = 20, sticky = "W")
sunset_time = Label(frame_sun, text = datetime.fromtimestamp(WeatherData["sys"]["sunset"]).strftime("%H:%M:%S"), font = ("Open Sans", time_size), bg = "#2b2b2b", fg = "white")
sunset_time.grid(row = 1, column = 3, padx = 20, sticky = "W")

# ---------------------------------- # 

def update_data():
    Response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ location + "&APPID=ab0ec2b1147266a1e70f838a21f450b8")
    WeatherData = Response.json()
    
    date_label.config(text = datetime.fromtimestamp(WeatherData["dt"]).strftime('%d.%m.%Y'))
    time_label.config(text = datetime.fromtimestamp(WeatherData["dt"]).strftime("%H:%M:%S"))
    
    temperatur.config(text = "{}°C".format(round(WeatherData["main"]["temp"] - 273, 1)))
    main_weather = WeatherData["weather"][0]["main"]
    if main_weather in ["Mist", "Fog", "Haze", "Smoke", "Dust", "Ash", "Squall", "Tornado", "Sand"]:
        main_weather = "Mist"
        
    weather_image = Image.open(f"/Users/hhemba334/Documents/Programmieren/GIT/python/rasp_weatherApp/IMG/{main_weather}.png")
    weather_resize = weather_image.resize((round(weather_image.size[0] / resize_factor), round(weather_image.size[1] / resize_factor)))
    weather_img = ImageTk.PhotoImage(weather_resize)
    
    temp_img.configure(image=weather_img)
    temp_img.image = weather_img
    
    temp_feel.config(text = "Gefühlt: {}°C".format(round(WeatherData["main"]["feels_like"] - 273, 1)))
    pressure.config(text = "Luftdruck: {} hPa".format(WeatherData["main"]["pressure"]))
    humid.config(text = "Luftfeuchtigkeit: {}%".format(WeatherData["main"]["humidity"]))
    
    sunrise_time.config(text = datetime.fromtimestamp(WeatherData["sys"]["sunrise"]).strftime("%H:%M:%S"))
    sunset_time.config(text = datetime.fromtimestamp(WeatherData["sys"]["sunset"]).strftime("%H:%M:%S"))         
    
    print("Update:" + time.strftime("%H:%M:%S"))
    root.after(600000, update_data)



update_data()
root.mainloop()
