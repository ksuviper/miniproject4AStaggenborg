from django.contrib import admin

from .models import Remedy, RemedyPotency, RemedyMateriaMedica, Potency, MateriaMedica

# Register your models here.
admin.site.register(Remedy)
admin.site.register(Potency)
admin.site.register(MateriaMedica)
