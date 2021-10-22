# Generated by Django 2.2.24 on 2021-10-22 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0002_car"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="car_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
