# Generated by Django 3.0.8 on 2020-09-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0007_auto_20200909_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='searchquery',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
