import requests
import json

API_KEY = 'e0bf2642fb0205464226e31038fc5c65'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(API_URL, params=params)
        data = json.loads(response.text)
        
        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            print(f'Weather forecast for {city}:')
            print(f'Description: {weather_description}')
            print(f'Temperature: {temperature}°C')
            print(f'Humidity: {humidity}%')
            print(f'Wind Speed: {wind_speed} m/s')
        elif response.status_code == 401:
            print('Unauthorized: Invalid API key. Please check your API key.')
        else:
            print(f'Error retrieving weather forecast for {city}.')
            print(f'Status Code: {response.status_code}')
    
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    city = input('Enter city name: ')
    get_weather(city)
