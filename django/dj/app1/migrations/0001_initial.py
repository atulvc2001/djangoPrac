# Generated by Django 5.0 on 2024-01-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="student",
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
                ("mob", models.IntegerField()),
                ("sid", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
