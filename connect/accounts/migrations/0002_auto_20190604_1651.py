# Generated by Django 2.2 on 2019-06-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(default=''),
        ),
    ]
