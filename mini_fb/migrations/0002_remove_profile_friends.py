# Generated by Django 3.2.8 on 2021-11-01 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
    ]
