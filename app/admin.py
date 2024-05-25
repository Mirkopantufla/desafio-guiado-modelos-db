from django.contrib import admin
from .models import Chofer, Vehiculo, RegistroContabilidad

# Register your models here.
admin.site.register(Chofer)
admin.site.register(Vehiculo)
admin.site.register(RegistroContabilidad)