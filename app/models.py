from django.db import models

# Create your models here.
class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    vehiculo = models.OneToOneField('Vehiculo', related_name='chofer',on_delete=models.PROTECT) #Cambio el nombre de vehiculo_id a patente_vehiculo para mas consistencia
    
    def __str__(self):
        return f"""{self.rut} - {self.nombre} {self.apellido} - Estado Activo: {self.activo} / Vehiculo: {self.vehiculo}"""
    

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6)
    marca = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"""{self.patente} - {self.marca} - {self.modelo} - {self.year} - Estado activo: {self.activo}"""

class RegistroContabilidad(models.Model):
    fecha_compra = models.DateField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    creacion_registro = models.DateField(auto_now_add=True)
    vehiculo = models.OneToOneField('Vehiculo', related_name='contabilidad',on_delete=models.PROTECT) #Cambio el nombre de vehiculo_id a patente_vehiculo para mas consistencia

    def __str__(self):
        return f"""{self.id} - {self.valor} / Vehiculo: {self.vehiculo}"""