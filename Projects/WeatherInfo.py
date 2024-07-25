import requests
import json

city = "Dhaka"
api_key = "df2bfc974e951c5152bd27ebc1a68460"  # api key in openweathermap.org
base_url = "https://api.openweathermap.org/data/2.5/weather?"
url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url)
x = response.json()
print(x, "\n")

if x['cod'] != 401:
    print("City Name : ", x['name'])
    print("Weather : ", x['weather'])
    print("Weather : ", x['weather'][0]['main'])
    print("Temp : ", x['main']['temp'])
    print("Minimum Temp : ", x['main']['temp_min'])
    print("Maximum Temp : ", x['main']['temp_max'])
else:
    print("City not found")

