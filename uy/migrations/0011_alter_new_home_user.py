# Generated by Django 3.2.9 on 2021-12-19 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uy', '0010_auto_20211219_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_home',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='uy.profile'),
        ),
    ]
