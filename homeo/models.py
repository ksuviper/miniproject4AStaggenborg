import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone


class PotencyList(models.Model):
    availablePotency = models.CharField(max_length=5)

    def __str__(self):
        return self.availablePotency


class MateriaMedica(models.Model):
    link = models.URLField()
    data = models.TextField()
    description = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.description


class Remedy(models.Model):
    name = models.CharField(max_length=50)

    potency = models.ManyToManyField(PotencyList)
    materiaMedica = models.ManyToManyField(MateriaMedica)

    def __str__(self):
        return self.name


