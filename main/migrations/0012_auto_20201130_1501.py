# Generated by Django 3.1.3 on 2020-11-30 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201128_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 15, 1, 40, 127376), verbose_name='date published'),
        ),
    ]
