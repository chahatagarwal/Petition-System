# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-15 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petitionstartdate', models.DateField()),
                ('petitiontitle', models.CharField(max_length=100)),
                ('petitionbackstory', models.TextField()),
                ('petitionsubtitle', models.CharField(max_length=255)),
                ('petitioncountyes', models.IntegerField(default=0)),
                ('petitioncountno', models.IntegerField(default=0)),
                ('petitionwhy', models.TextField()),
                ('petitionprooflink', models.TextField()),
                ('petitionlocation', models.TextField()),
                ('petitionthershold', models.IntegerField()),
                ('petitionstatus', models.BooleanField(default=True)),
                ('petitioncountview', models.IntegerField(default=0)),
                ('petitiontotalengagement', models.IntegerField(default=0)),
            ],
        ),
    ]