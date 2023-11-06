# Name: Matthew Walters & Andrew Etheridge
# Email: waltemw@mail.uc.edu, etheriaw@mail.uc.edu
# Assignment Title: Assignment 10 
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Create a entry point to go and grab some data via API     
# Citations: https://uc.instructure.com/courses/1640384/pages/learning-materials-9?module_item_id=70078231 - in class code,
#            https://stackoverflow.com/questions/16401906/how-to-pair-up-two-lists - used for using the 'in zip' within for my for loop
# Anything else that's relevant: Used the JSON python code provided in the lecture slides 
# main.py

from functionPackage.function import *

if __name__ == "__main__":
    weatherData = getWeatherData()
    timestamps, temperatures = parseWeatherData(weatherData)

    print("Your Cincinnati Temperature Forecast Hourly for the next 7 days")

    for timestamp, temperature in zip(timestamps, temperatures):
        print(f"Date & Hour: {timestamp} Temperature: {temperature}°F")
