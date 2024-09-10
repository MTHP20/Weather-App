import requests 
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def get_lan_lon(city_name,state_code,country_code,API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon
    
def get_current_weather(lat, lon, API_key):
    resp = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')

print(get_lan_lon('Toronto', 'ON', 'Canada', api_key))