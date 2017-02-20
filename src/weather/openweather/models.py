from django.db import models


class OpenWeather(models.Model):
    city = models.CharField(max_length=150)
    city_id = models.IntegerField()
    country = models.CharField(max_length=50, default='', blank=True)
    lon = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    temp = models.FloatField(null=True, blank=True)
    temp_min = models.FloatField(null=True, blank=True)
    temp_max = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    visibility = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    wind_deg = models.FloatField(null=True, blank=True)
    sunrise = models.DateTimeField(null=True, blank=True)
    sunset = models.DateTimeField(null=True, blank=True)
    weather = models.CharField(max_length=50, default='', blank=True)
    description = models.CharField(max_length=250, default='', blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('city', 'city_id')]

    def __str__(self):
        return '<OpenWeather city={} country={} weather={}>'.format(
            self.city, self.country, self.weather)
