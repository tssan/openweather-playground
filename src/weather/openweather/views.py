from django.http import HttpResponse

from .serializers import weather_to_json, weather_to_xml
from .apicall import get_weather


def prep_resp(format, weather):
    valid_content_types = ['json', 'xml']
    if format not in valid_content_types:
        raise TypeError('Invalid format')
    if format == 'json':
        content_type = 'application/json'
        content = weather_to_json(weather)
    if format == 'xml':
        content_type = 'application/xml'
        content = weather_to_xml(weather)
    return content_type, content


def weather(request):
    if request.method == 'GET':
        output_format = 'json'
        weather = None
        if 'format' in request.GET:
            output_format = request.GET['format']

        if 'city' in request.GET:
            weather = get_weather(request.GET['city'].lower())

        ct, content = prep_resp(output_format, weather)
        return HttpResponse(content, content_type=ct)
    return HttpResponse({})
