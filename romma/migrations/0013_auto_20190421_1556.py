# Generated by Django 2.1.7 on 2019-04-21 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romma', '0012_auto_20190421_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 21, 15, 56, 0, 711086)),
        ),
    ]
