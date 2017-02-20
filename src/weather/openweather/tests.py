from http import HTTPStatus

from django.test import TestCase
from django.core.urlresolvers import reverse


class OpenWeatherTest(TestCase):
    def setUp(self):
        self.url = reverse('weather')

    def test_response_format(self):
        response = self.client.get(self.url + '?q=krakow&format=json')
        self.assertEqual(response.status_code, HTTPStatus.OK.value)
        self.assertEqual(response._headers['content-type'][1], 'application/json')

        response = self.client.get(self.url + '?q=krakow&format=xml')
        self.assertEqual(response.status_code, HTTPStatus.OK.value)
        self.assertEqual(response._headers['content-type'][1], 'application/xml')
