from django.db import models
from  django.contrib.auth.models import User


class Medico(models.Model):  

    id = models.IntegerField(primary_key=True)  #PK sin autoincremento
    contraseña = = models.charField(max_length = 100)
    nombre = models.CharField(max_length= 100)
    apellidos = models.charField(max_length = 100)
    telefono = models.charField(max_length = 100)
    correo = = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    especialidad = models.charField(max_length = 100)
    rol = models.IntegerField()   #según tabla Roles
    FK_especialidad =  models.ForeignKey(Especialidad, editable=False, on_delete=models.CASCADE) 
    FK_autorizacion = models.ForeignKey(Autorizaciones, editable=False, on_delete=models.CASCADE) 
    FK_orden = models.ForeignKey(Ordenes, editable=False, on_delete=models.CASCADE) 
    FK_roles = models.ForeignKey(Roles, editable=False, on_delete=models.CASCADE) 


class Paciente(models.Model):
    id = models.IntegerField(primary_key=True)
    contraseña = models.charField(max_length = 100)
    nombre = models.charField(max_length = 100)
    apellidos = models.charField(max_length = 100)
    telefono = models.charField(max_length = 100)
    correo = models.EmailField(max_length=)
    fecha_nacimiento = models.DateField()
    dias_incapacidad = models.charField(max_length = 100)
    resultados_examenes = models.TextField()
    rol = models.IntegerField()      #según tabla Roles
    FK_medico = models.ForeignKey(Medico, editable=False, on_delete=models.CASCADE) 
    FK_grupoFamiliar = models.ForeignKey(Solicitud_grupoFam, editable=False, on_delete=models.CASCADE) 
    FK_roles = models.ForeignKey(Roles, editable=False, on_delete=models.CASCADE) 
    FK_cambioMedico = models.ForeignKey(Solicitud_cambioMedico, editable=False, on_delete=models.CASCADE)
    FK_autorizacion = models.ForeignKey(Autorizacione, editable=False, on_delete=models.CASCADE)


class HistoriaClinica(models.Model):
    id = models.IntegerField(primary_key=True)
    date_aperturaHist = models.TimeField()
    FK_paciente = models.ForeignKey(Paciente, editable=False, on_delete=models.CASCADE)
    FK_diagnostico = models.ForeignKey(Diagnostico, editable=False, on_delete=models.CASCADE)
    FK_ordenes = models.ForeignKey(Ordenes, editable=False, on_delete=models.CASCADE)
    FK_medico = models.ForeignKey(Medico, editable=False, on_delete=models.CASCADE)

class Diagnostico(models.Model):
    id = models.IntegerField(primary_key=True)
    sintomas = models.charField(max_length = 500)
    resultado_diagnos = models.charField(max_length = 500)
    fecha = models.DateField
    FK_paciente = models.ForeignKey(Paciente, editable=False, on_delete=models.CASCADE)
    

class Interaccion(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion_mensaje = models.charField(max_length = 500)
    fecha = models.DateField()
    FK_paciente = models.ForeignKey(Paciente, editable=False, on_delete=models.CASCADE)
    FK_medico = models.ForeignKey(Medico, editable=False, on_delete=models.CASCADE)

class Solicitud_grupoFam(models.Model):
    id = models.AutoField(primary_key=True)
    id_grupo = models.AutoField()
    

class Solicitud_cambioMedico(models.Model):
    id = models.AutoField(primary_key=True)

class Ordenes(models.Model):
    id = models.AutoField(primary_key=True)

class Autorizaciones(models.Model):
    id = models.AutoField(primary_key=True)

class Roles(models.Model):
    id = models.AutoField(primary_key=True)

class Especialidad(models.Model):
    id = models.AutoField(primary_key=True)