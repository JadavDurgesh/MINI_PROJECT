# Generated by Django 4.2.3 on 2023-08-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
                ("username", models.CharField(max_length=50)),
                ("f_name", models.CharField(max_length=80)),
                ("l_name", models.CharField(max_length=80)),
                ("contact", models.CharField(max_length=80)),
                ("address", models.CharField(max_length=500)),
            ],
        ),
    ]
