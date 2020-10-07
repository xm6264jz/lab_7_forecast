import os
import requests
from datetime import datetime
import logging

key = os.environ.get('WEATHER_KEY')
 
url = 'http://api.openweathermap.org/data/2.5/forecast'

def main():

    location = get_location()
    weather_data, error = get_current_weather(location, key)
    
    print(weather_data)

    current_temp = get_temp()

    print(f'The current temperature is {current_temp} C')
    get_description(weather_description=description)
    get_speed(wind_speed=speed)
    logging.info('Query successful')

def get_location():
    city, country = '',''
    while len(city) == 0:
        city = input('Please enter the city: ').strip()

    while len(country) !=2 or not country.isalpha():
        country = input('Enter the 2 letter country code: ')
    location = f'{city}, {country}'
    return location

def get_current_weather(location, key):
   
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key }
        response = requests.get(url, params=query)
        response.raise_for_status()
        data = response.json()
        return data, None
    except Exception as ex:
        logging.exception(ex)
        logging.info(response.text)
        return None, ex

def get_temp(weather_temp):
    list_of_forecasts = weather_temp['list']
    for forecast in list_of_forecasts:

        temp = forecast['main'] ['temp']
        timestamp = forecast['dt_txt']
        forecast_date = datetime.fromtimestamp(timestamp)
        print (f'At {forecast_date} the temperature will be {temp} C')

def get_description(weather_description):
    
    try:
        temp = weather_description['weather']['description']
        return temp
    except KeyError:
        logging.exception('This data is not in the format expected')
        return 'Unknown'

def get_speed(wind_speed):
    
    try:
        temp = wind_speed['wind']['speed']
        return temp
    except KeyError:
        logging.exception('This data is not in the format expected')
        return 'Unknown'

if __name__ == "__main__":
    main()

