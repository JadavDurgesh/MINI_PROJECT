# Generated by Django 4.2.3 on 2023-08-10 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="otp",
            field=models.IntegerField(default=1234),
        ),
    ]
