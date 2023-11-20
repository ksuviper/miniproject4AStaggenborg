import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone


class Potency(models.Model):
    potency = models.CharField(max_length=5)

    def __str__(self):
        return self.potency


class MateriaMedica(models.Model):
    link = models.URLField()
    data = models.TextField()
    description = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.link


class Remedy(models.Model):
    name = models.CharField(max_length=50)
    potency = models.ManyToManyField(Potency)
    materiaMedia = models.ManyToManyField(MateriaMedica)

    def __str__(self):
        return self.name


# class RemedyPotency(models.Model):
#     remedy = models.ForeignKey(Remedy, on_delete=models.CASCADE)
#     potency = models.ManyToManyField(Potency)
#
#     def __str__(self):
#         return self.remedy + " (" + self.potency + ")"


class RemedyMateriaMedica(models.Model):
    remedy = models.ForeignKey(Remedy, on_delete=models.CASCADE)
    materiaMedica = models.ForeignKey(MateriaMedica, on_delete=models.RESTRICT)
    description = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.materiaMedica


