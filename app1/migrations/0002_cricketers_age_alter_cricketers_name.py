# Generated by Django 4.2.6 on 2023-12-20 14:04

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cricketers",
            name="age",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="cricketers",
            name="name",
            field=models.CharField(
                max_length=250, validators=[app1.models.check_spcial_symbols]
            ),
        ),
    ]