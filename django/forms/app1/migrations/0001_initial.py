# Generated by Django 5.0 on 2024-01-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="sample",
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
                ("name", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("dob", models.DateField()),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
