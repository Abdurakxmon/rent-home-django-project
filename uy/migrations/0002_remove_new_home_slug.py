# Generated by Django 3.2.9 on 2021-12-19 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_home',
            name='slug',
        ),
    ]
