# Generated by Django 2.1.7 on 2019-03-29 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romma', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy',
            old_name='buy',
            new_name='month_plan',
        ),
        migrations.AlterField(
            model_name='buy',
            name='end_at',
            field=models.DateField(default=datetime.datetime(2019, 4, 28, 16, 49, 17, 670086)),
        ),
        migrations.AlterField(
            model_name='buy',
            name='started_at',
            field=models.DateField(default=datetime.datetime(2019, 3, 29, 16, 49, 17, 670056)),
        ),
    ]
