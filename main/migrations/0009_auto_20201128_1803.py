# Generated by Django 3.1.3 on 2020-11-28 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201128_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 18, 3, 4, 573107), verbose_name='date published'),
        ),
    ]
