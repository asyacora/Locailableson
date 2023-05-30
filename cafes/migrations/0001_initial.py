# Generated by Django 4.1.7 on 2023-05-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Business",
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
                ("cafeId", models.UUIDField()),
                ("email", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=200)),
                ("neighborhood", models.CharField(max_length=100)),
                ("capacity", models.IntegerField()),
                ("available_capacity", models.IntegerField()),
            ],
        ),
    ]
