# Generated by Django 2.2 on 2019-06-02 09:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('main', '0006_auto_20190602_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='tut_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 2, 15, 28, 40, 684701), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tut_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Series', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tut_slug',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
