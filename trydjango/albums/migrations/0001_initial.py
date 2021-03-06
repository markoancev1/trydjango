# Generated by Django 3.1.3 on 2020-11-13 15:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('singers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=25)),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('released', models.BooleanField(default=False)),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singers.singer')),
            ],
        ),
    ]
