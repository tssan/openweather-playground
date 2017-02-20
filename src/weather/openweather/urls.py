from django.conf.urls import url

from .views import weather


urlpatterns = [
    url(r'^/?$', weather, name="weather")
]
