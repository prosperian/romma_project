# Generated by Django 2.1.7 on 2019-04-23 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romma', '0014_auto_20190423_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 12, 32, 57, 937471)),
        ),
    ]