from django.db import models
from django.http import request


class Room(models.Model):
    id = models.BigAutoField(primary_key=True)
    room_name = models.CharField(max_length=64, null=False)
    room_capacity = models.SmallIntegerField
    projector = models.BooleanField


# Create your models here.
