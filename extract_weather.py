import requests
import pandas as pd

def get_weather(city, lat, lon):
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {'latitude': lat, 'longitude': lon, 'hourly': 'temperature_2m,precipitation,wind_speed_10m', 'past_days': 7, 'timezone': 'Europe/London'}
    # data = requests.get(url, params=params).json()
    data = requests.get(url, params=params, timeout=30).json()
    return pd.DataFrame({'city': city, 'datetime': data['hourly']['time'], 'temp_c': data['hourly']['temperature_2m'], 'rain_mm': data['hourly']['precipitation']})

cities = [('London',51.5074,-0.1278),('Manchester',53.4808,-2.2426),('Birmingham',52.4862,-1.8904),('Edinburgh',55.9533,-3.1883)]
df = pd.concat([get_weather(*c) for c in cities], ignore_index=True)
print('Extracted ' + str(len(df)) + ' rows')
print(df.head())

