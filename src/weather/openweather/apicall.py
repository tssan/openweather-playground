import datetime
import requests

from django.conf import settings

from .models import OpenWeather


def get_weather_by_city_name(cityname):
    response = requests.get(
        settings.OPENWEATHER_URI,
        params={
            'q': cityname,
            'APPID': settings.OPENWEATHER_API_KEY
        }
    )
    return response.json()


def get_openweather(city):
    openweather = get_weather_by_city_name(city)
    weather, _created = OpenWeather.objects.get_or_create(
        city=openweather['name'],
        city_id=openweather['id']
    )
    weather.country = openweather['sys']['country']
    weather.lon = openweather['coord']['lon']
    weather.lat = openweather['coord']['lat']
    weather.temp = openweather['main']['temp']
    weather.temp_min = openweather['main']['temp_min']
    weather.temp_max = openweather['main']['temp_max']
    weather.pressure = openweather['main']['pressure']
    weather.humidity = openweather['main']['humidity']
    weather.visibility = openweather.get('visibility', None)
    weather.wind_speed = openweather['wind']['speed']
    weather.wind_def = openweather['wind']['deg']
    weather.sunrise = datetime.datetime.fromtimestamp(openweather['sys']['sunrise'])
    weather.sunset = datetime.datetime.fromtimestamp(openweather['sys']['sunset'])
    weather.weather = openweather['weather'][0]['main']
    weather.description = openweather['weather'][0]['description']
    weather.save()
    return weather


def get_weather(city):
    try:
        hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)
        weather = OpenWeather.objects.get(city=city, created_at__lte=hour_ago)
    except OpenWeather.DoesNotExist:
        weather = get_openweather(city)
    return weather
