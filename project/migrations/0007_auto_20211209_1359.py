# Generated by Django 3.1.6 on 2021-12-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20211208_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='full_name',
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.CharField(max_length=30),
        ),
    ]
