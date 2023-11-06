# Name: Matthew Walters & Andrew Etheridge
# Email: waltemw@mail.uc.edu, etheriaw@mail.uc.edu
# Assignment Title: Assignment 10 
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Created some functions to be invoked in the main      
# Citations: https://uc.instructure.com/courses/1640384/pages/learning-materials-9?module_item_id=70078231 - in class code,
# Anything else that's relevant: Used the JSON python code provided in the lecture slides 
# fucntion.py


import json
import requests

# function to pull the data via api. Thanks for the in class code!
def getWeatherData ():
    # API that displays 7 Day range of Cincinnati's temperature 
    response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=39.1271&longitude=-84.5144&hourly=temperature_2m&temperature_unit=fahrenheit&windspeed_unit=mph')
    json_string = response.content
    parsed_json = json.loads(json_string)
    return parsed_json

# function to parse to the data and return it in a legiable format
def parseWeatherData(parsed_json):
    # Extracting the hourly time stamps and temperatures from the parsed JSON data
    hourly_data = parsed_json['hourly']
    timestamps = hourly_data['time']
    temperatures = hourly_data['temperature_2m']
    return timestamps, temperatures