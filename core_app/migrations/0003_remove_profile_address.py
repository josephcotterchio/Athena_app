# Generated by Django 3.0.8 on 2020-09-08 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_auto_20200908_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
    ]
