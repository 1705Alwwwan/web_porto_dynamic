# Generated by Django 5.1.4 on 2025-02-16 05:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bio", "0010_kindskill"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Skill",
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
                ("skill_name", models.CharField(max_length=100)),
                ("date_posted", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "kind_skill",
                    models.ForeignKey(
                        max_length=100,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bio.kindskill",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        max_length=20,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
