from django.conf import settings
from django.db import models


class Car(models.Model):
    "Generated Model"
    num = models.BigIntegerField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="car_user",
    )
