from django.conf import settings
from django.db import models


class Car(models.Model):
    "Generated Model"
    num = models.BigIntegerField()
