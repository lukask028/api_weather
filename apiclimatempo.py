import requests 
from pprint import pprint

api_key = '9e55fa704c8f4706e2e9120bde0a6e57'

city = input('Digite uma cidade:')

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
