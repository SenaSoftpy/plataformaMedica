from django.db import models


class Medico(models.Model):  

    id = models.AutoField(primary_key=True)
    contraseña = = models.charField(max_length = 100)
    nombre = models.CharField(max_length= 100)
    apellidos = models.charField(max_length = 100)
    telefono = models.charField(max_length = 100)
    correo = = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)

class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True)

class Diagnostico(models.Model):
    id = models.AutoField(primary_key=True)

class Interaccion(models.Model):
    id = models.AutoField(primary_key=True)

class Solicitud_grupoFam(models.Model):
    id = models.AutoField(primary_key=True)

class Solicitud_cambioMedico(models.Model):
    id = models.AutoField(primary_key=True)

class Ordenes(models.Model):
    id = models.AutoField(primary_key=True)

class Autorizaciones(models.Model):
    id = models.AutoField(primary_key=True)

class Roles(models.Model):
    id = models.AutoField(primary_key=True)