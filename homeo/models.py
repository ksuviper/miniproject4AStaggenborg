import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone


class Remedy(models.Model):
    name = models.CharField(max_length=50)
    lastUpdated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name


class PotencyList(models.Model):
    availablePotency = models.CharField(max_length=5)

    def __str__(self):
        return self.availablePotency


class Potency(models.Model):
    remedy = models.ForeignKey(Remedy, on_delete=models.CASCADE)
    potency = models.ForeignKey(PotencyList, on_delete=models.CASCADE)

    def __str__(self):
        return self.remedy.name + " " + self.potency.availablePotency


class MateriaMedica(models.Model):
    remedy = models.ForeignKey(Remedy, on_delete=models.CASCADE)
    link = models.URLField()
    data = models.TextField()
    description = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.description


# class RemedyPotency(models.Model):
#     remedy = models.ForeignKey(Remedy, on_delete=models.CASCADE)
#     potency = models.ManyToManyField(Potency)
#
#     def __str__(self):
#         return self.remedy + " (" + self.potency + ")"


# class RemedyMateriaMedica(models.Model):
#     remedy = models.ForeignKey(Remedy, on_delete=models.CASCADE)
#     materiaMedica = models.ForeignKey(MateriaMedica, on_delete=models.RESTRICT)
#     description = models.CharField(max_length=100, default="")
#
#     def __str__(self):
#         return self.materiaMedica


