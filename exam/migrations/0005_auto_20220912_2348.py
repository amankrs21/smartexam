# Generated by Django 3.2.12 on 2022-09-12 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20220912_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinfo',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 23, 48, 16, 100503)),
        ),
        migrations.AlterField(
            model_name='examinfo',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 23, 48, 16, 100476)),
        ),
    ]