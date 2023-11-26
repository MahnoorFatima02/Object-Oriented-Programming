import requests
import json

city_name = input("Enter your city here: ")
apiid = "9ee76e91aeb30d199324f9e91b080fde"

request = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + apiid
try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        kelvin_temperature = json_response["main"]["temp"]
        celsius_temperature = float(kelvin_temperature) - 273.15
        print(round(celsius_temperature, 2))

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")



