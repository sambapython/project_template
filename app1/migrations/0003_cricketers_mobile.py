# Generated by Django 4.2.6 on 2023-12-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0002_cricketers_age_alter_cricketers_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="cricketers",
            name="mobile",
            field=models.CharField(default="0000000000", max_length=15),
        ),
    ]
