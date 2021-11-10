from django.db import models

# Create your models here.

class pelicula(models.Model):
    idPeli = models.AutoField(primary_key = True)
    titulo = models.CharField('Nombre de la Pelicula', max_length = 50, null = False, blank = False)
    categoria = models.CharField('Enfoque de la Pelicula', max_length = 30 ,null = False, blank = False)
    fech_alquiler = models.DateField('Fecha Alquiler', null = False, blank = False)
    fech_devol = models.DateField('Fecha Devolucion', null = False, blank = False)

    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'

class cliente(models.Model):
    idcli = models.AutoField(primary_key = True)
    dni = models.CharField('DNI cliente', max_length = 9, null = False, blank = False)
    nombre = models.CharField('Nombre cliente', max_length = 20, null = False, blank = False)
    apellidos = models.CharField('Apellidos cliente', max_length = 30, null = False, blank = False)
    telefono = models.CharField('telefono cliente', max_length = 9, null = False, blank = False)
    

