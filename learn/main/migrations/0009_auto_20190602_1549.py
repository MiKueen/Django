# Generated by Django 2.2 on 2019-06-02 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('main', '0008_auto_20190602_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 2, 15, 49, 57, 845449), verbose_name='date published'),
        ),
    ]