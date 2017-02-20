import json

from django.template import Context, loader


def weather_to_dict(weather):
    if weather:
        return {
            'pk': weather.pk,
            'city': weather.city,
            'city_id': weather.city_id,
            'country': weather.country,
            'lon': weather.lon,
            'lat': weather.lat,
            'temp': weather.temp,
            'temp_min': weather.temp_min,
            'temp_max': weather.temp_max,
            'pressure': weather.pressure,
            'humidity': weather.humidity,
            'visibility': weather.visibility,
            'wind_speed': weather.wind_speed,
            'wind_deg': weather.wind_deg,
            'sunrise': str(weather.sunrise),
            'sunset': str(weather.sunset),
            'weather': weather.weather,
            'description': weather.description,
            'created_at': str(weather.created_at)
        }


def weather_to_xml(weather):
    context = Context({'weather': weather_to_dict(weather)})
    tpl = loader.get_template('weather.xml')
    return tpl.render(context)


def weather_to_json(weather):
    return json.dumps({'wheater': weather_to_dict(weather)})
