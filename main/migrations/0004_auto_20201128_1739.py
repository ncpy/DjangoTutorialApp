# Generated by Django 3.1.3 on 2020-11-28 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201128_1736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorialseries',
            options={'verbose_name_plural': 'Series'},
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 17, 39, 17, 277547), verbose_name='date published'),
        ),
    ]
