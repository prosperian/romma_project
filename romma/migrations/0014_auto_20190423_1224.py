# Generated by Django 2.1.7 on 2019-04-23 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romma', '0013_auto_20190421_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 12, 24, 7, 889321)),
        ),
    ]
