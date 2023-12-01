from django.contrib import admin
from .models import Remedy, MateriaMedica, PotencyList


# Register your models here.
admin.site.register(Remedy)
admin.site.register(MateriaMedica)
admin.site.register(PotencyList)
