# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-16 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logistic_Regression', models.IntegerField()),
                ('Decison_Tree', models.IntegerField()),
                ('K_nearestNeighbour', models.IntegerField()),
                ('size_of_x_train', models.IntegerField()),
                ('size_of_y_train', models.IntegerField()),
            ],
        ),
    ]