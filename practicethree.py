import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import requests

Window.size = (600,600)

class mygrid(BoxLayout):
    city = ObjectProperty(None)
    temperature = ''
    air_pressure = ''
    moisture_percentage = ''
    wind_speed = ''
    wind_direction = ''
    emotional_temperature = ''
    weather_description = ''

    def btn(self):
        api_key = "a8364bc75d31d599ab8bc9adbc3171f9"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + self.city.text
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main_data = data["main"]
            weather_data = data["weather"][0]

            self.temperature = str(main_data["temp"])
            self.air_pressure = str(main_data["pressure"])
            self.moisture_percentage = str(main_data["humidity"])
            self.wind_speed = str(data["wind"]["speed"])
            self.wind_direction = str(data["wind"]["deg"])
            self.emotional_temperature = str(main_data["feels_like"])
            self.weather_description = str(weather_data["description"])

        else:
            print("City Not Found")

        self.update_labels()

    def update_labels(self):
        self.ids.temperature_label.text = self.temperature
        self.ids.air_pressure_label.text = self.air_pressure
        self.ids.moisture_label.text = self.moisture_percentage
        self.ids.wind_speed_label.text = self.wind_speed
        self.ids.wind_direction_label.text = self.wind_direction
        self.ids.emotional_temperature_label.text = self.emotional_temperature
        self.ids.weather_desc_label.text = self.weather_description

class Weather(App):
    def build(self):
        return mygrid()

if __name__ == '__main__':
    Weather().run()