# Generated by Django 3.1.3 on 2020-11-16 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singers', '0004_singer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]