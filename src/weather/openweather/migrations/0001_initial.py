# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=150)),
                ('city_id', models.IntegerField()),
                ('country', models.CharField(blank=True, default='', max_length=50)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('temp', models.FloatField(blank=True, null=True)),
                ('temp_min', models.FloatField(blank=True, null=True)),
                ('temp_max', models.FloatField(blank=True, null=True)),
                ('pressure', models.FloatField(blank=True, null=True)),
                ('humidity', models.FloatField(blank=True, null=True)),
                ('visibility', models.FloatField(blank=True, null=True)),
                ('wind_speed', models.FloatField(blank=True, null=True)),
                ('wind_deg', models.FloatField(blank=True, null=True)),
                ('sunrise', models.DateTimeField(blank=True, null=True)),
                ('sunset', models.DateTimeField(blank=True, null=True)),
                ('weather', models.CharField(blank=True, default='', max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='openweather',
            unique_together=set([('city', 'city_id')]),
        ),
    ]