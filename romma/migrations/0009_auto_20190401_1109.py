# Generated by Django 2.1.7 on 2019-04-01 11:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('romma', '0008_auto_20190331_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='buy',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 1, 11, 9, 26, 267451)),
        ),
    ]