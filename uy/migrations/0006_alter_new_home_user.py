# Generated by Django 3.2.9 on 2021-12-19 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uy', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_home',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uy.profile'),
        ),
    ]
