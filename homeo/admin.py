from django.contrib import admin

from .models import Remedy, Potency, MateriaMedica, PotencyList

# Register your models here.
admin.site.register(Remedy)
admin.site.register(Potency)
admin.site.register(MateriaMedica)
admin.site.register(PotencyList)