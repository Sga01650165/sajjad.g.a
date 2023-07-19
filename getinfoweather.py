import requests, json
api_key = "a8364bc75d31d599ab8bc9adbc3171f9"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
def name(city_name):
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        temperature = str(y["temp"])
        air_pressure = str(y["pressure"])
        moisture_percentage= str(y["humidity"])
        z = x["weather"]
        wind_speed = str(x["wind"]["speed"])
        wind_direction = str(x["wind"]["deg"])
        emotional_temperature = str(y["feels_like"])
        weather_description = str(z[0]["description"])
    else:
        print(" City Not Found ")