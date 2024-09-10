import requests 

def get_lan_lon():
    resp = requests.get('http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}')
