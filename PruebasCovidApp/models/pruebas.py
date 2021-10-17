from django.db                  import models


class Pruebas(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido =  models.CharField(max_length = 30)
    id = models.BigIntegerField(primary_key = True, unique = True)
    celular = models.BigIntegerField
    fijo = models.IntegerField
    email = models.CharField(max_length = 25)
    departamento = models.CharField(max_length = 25)
    municipio = models.CharField(max_length = 25)
    direccion = models.CharField(max_length = 80)
    resultado = models.CharField(max_length = 8)

