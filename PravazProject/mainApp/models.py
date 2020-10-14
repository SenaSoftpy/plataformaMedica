from django.db import models
from  django.contrib.auth.models import User


class Medico(models.Model):  

    id_medico = models.IntegerField(primary_key=True)  #PK sin autoincremento
    contraseña = models.CharField(max_length = 100)
    nombre = models.CharField(max_length= 100)
    apellidos = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 100)
    correo =  models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    especialidad = models.CharField(max_length = 100)
    rol = models.IntegerField()   #según tabla Roles
    FK_especialidad =  models.ForeignKey(id_especia, editable=False, on_delete=models.CASCADE) 
    FK_autorizacion = models.ForeignKey(id_autoriza, editable=False, on_delete=models.CASCADE) 
    FK_orden = models.ForeignKey(Ordenes, editable=False, on_delete=models.CASCADE) 
    FK_roles = models.ForeignKey(Roles, editable=False, on_delete=models.CASCADE) 


class Paciente(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    contraseña = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 100)
    correo = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    dias_incapacidad = models.CharField(max_length = 100)
    resultados_examenes = models.TextField()
    rol = models.IntegerField()      #según tabla Roles
    FK_medico = models.ForeignKey(Medico, editable=False, on_delete=models.CASCADE) 
    FK_grupoFamiliar = models.ForeignKey(Solicitud_grupoFam, editable=False, on_delete=models.CASCADE) 
    FK_roles = models.ForeignKey(Roles, editable=False, on_delete=models.CASCADE) 
    FK_cambioMedico = models.ForeignKey(Solicitud_cambioMedico, editable=False, on_delete=models.CASCADE)
    FK_autorizacion = models.ForeignKey(Autorizacione, editable=False, on_delete=models.CASCADE)


class HistoriaClinica(models.Model):
    id_historia = models.IntegerField(primary_key=True)
    date_aperturaHist = models.TimeField()
    FK_paciente = models.ForeignKey(Paciente, editable=False, on_delete=models.CASCADE)
    FK_diagnostico = models.ForeignKey(Diagnostico, editable=False, on_delete=models.CASCADE)
    FK_ordenes = models.ForeignKey(Ordenes, editable=False, on_delete=models.CASCADE)
    FK_medico = models.ForeignKey(Medico, editable=False, on_delete=models.CASCADE)

class Diagnostico(models.Model):
    id_diagnostico = models.IntegerField(primary_key=True)
    sintomas = models.CharField(max_length = 500)
    resultado_diagnos = models.CharField(max_length = 500)
    fecha = models.DateField
    FK_paciente = models.ForeignKey(Paciente, editable=False, on_delete=models.CASCADE)
    

class Interaccion(models.Model):
    id_interaccion = models.AutoField(primary_key=True)
    descripcion_mensaje = models.CharField(max_length = 500)
    fecha = models.DateField()
    FK_paciente = models.ForeignKey(Paciente, editable=False, on_delete=models.CASCADE)
    FK_medico = models.ForeignKey(Medico, editable=False, on_delete=models.CASCADE)

class Solicitud_grupoFam(models.Model):
    id_solicFam = models.AutoField(primary_key=True)
    id_grupo = models.AutoField()
    integrantes = models.TextField()
    FK_paciente = models.ForeignKey(Paciente, editable=False, on_delete=models.CASCADE)


class Solicitud_cambioMedico(models.Model):
    id_solicMed = models.AutoField(primary_key=True)
    motivo = models.TextField()
    medico_actual = models.IntegerField()
    FK_paciente = models.ForeignKey(Paciente, editable=False, on_delete=models.CASCADE)

class Ordenes(models.Model):
    id_orden = models.AutoField(primary_key=True)
    idAutorización = models.AutoField()
    nombre_paciente = models.CharField(max_length = 100)
    identificacion = models.CharField(max_length = 100)
    correo = models.EmailField(max_length=100)
    descripcion = models.TextField()

class Autorizaciones(models.Model):
    id_autoriza = models.AutoField(primary_key=True)
    tipo_autorizacion = models.CharField(max_length = 100)
    FK_paciente = models.ForeignKey(Paciente, editable=False, on_delete=models.CASCADE)
    FK_medico = models.ForeignKey(Medico, editable=False, on_delete=models.CASCADE)

class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.IntegerField()

class Especialidad(models.Model):
    id_especia = models.AutoField(primary_key=True)
    especialidad = models.CharField(max_length = 100)
