from django.db import models

class Especialidad(models.Model):
#   id_rol = models.AutoField(primary_key=True)
  especialidad = models.IntegerField()


class Solicitud_grupoFam(models.Model):
#   id_solicFam = models.AutoField(primary_key=True)
  idGrupoFam = models.IntegerField()
  integrantes = models.TextField()


class Ordenes(models.Model):
#   id_orden = models.AutoField(primary_key=True)
  idAutorización = models.IntegerField()
  nombre_paciente = models.CharField(max_length = 100)
  identificacion = models.CharField(max_length = 100)
  correo = models.EmailField(max_length=100)
  descripcion = models.TextField()

class Roles(models.Model):
#   id_rol = models.AutoField(primary_key=True)
  rol = models.IntegerField()

class Medico(models.Model):  

#  id_medico = models.IntegerField(primary_key=True)  #PK sin autoincremento
  contrasena = models.CharField(max_length = 100)
  nombre = models.CharField(max_length= 100)
  apellidos = models.CharField(max_length = 100)
  telefono = models.CharField(max_length = 100)
  correo =  models.EmailField(max_length=100)
  fecha_nacimiento = models.DateField()
  especialidad = models.CharField(max_length = 100)
  rol = models.IntegerField()   #según tabla Roles
  FK_especialidad =  models.ForeignKey(Especialidad, null = True, editable=False, on_delete=models.CASCADE) 
  FK_orden = models.ForeignKey(Ordenes, null = True, editable=False, on_delete=models.CASCADE) 
  FK_roles = models.ForeignKey(Roles, null = True, editable=False, on_delete=models.CASCADE) 

class Autorizaciones(models.Model):
#   id_autorizacion = models.AutoField(primary_key=True)
  tipo_autorizacion = models.CharField(max_length = 100)
  FK_medico = models.ForeignKey(Medico, null = True, editable=False, on_delete=models.CASCADE)



class Paciente(models.Model):
  # id_paciente = models.IntegerField(primary_key=True)
  contrasena = models.CharField(max_length = 100)
  nombre = models.CharField(max_length = 100)
  apellidos = models.CharField(max_length = 100)
  telefono = models.CharField(max_length = 100)
  correo = models.EmailField(max_length=100)
  fecha_nacimiento = models.DateField()
  dias_incapacidad = models.CharField(max_length = 100)
  resultados_examenes = models.TextField()
  rol = models.IntegerField()      #según tabla Roles
  FK_medico = models.ForeignKey(Medico, null = True, editable=False, on_delete=models.CASCADE) 
  FK_grupoFamiliar = models.ForeignKey(Solicitud_grupoFam, null = True, editable=False, on_delete=models.CASCADE) 
  FK_roles = models.ForeignKey(Roles, editable=False, null = True, on_delete=models.CASCADE) 
  FK_autorizacion = models.ForeignKey(Autorizaciones, null = True, editable=False, on_delete=models.CASCADE)

class Diagnostico(models.Model):
#  id_diagnostico = models.IntegerField(primary_key=True)
  sintomas = models.CharField(max_length = 500)
  resultado_diagnos = models.CharField(max_length = 500)
  fecha = models.DateField
  FK_paciente = models.ForeignKey(Paciente, editable=False, null = True, on_delete=models.CASCADE)
  
class Solicitud_cambioMedico(models.Model):
#    id_solicMed = models.AutoField(primary_key=True)
  motivo = models.TextField()
  medico_actual = models.IntegerField()
  FK_paciente = models.ForeignKey(Paciente, editable=False, null = True, on_delete=models.CASCADE)

class HistoriaClinica(models.Model):
#  id_historia = models.IntegerField(primary_key=True)
  date_aperturaHist = models.TimeField()
  FK_paciente = models.ForeignKey(Paciente, null = True, editable=False, on_delete=models.CASCADE)
  FK_diagnostico = models.ForeignKey(Diagnostico, null = True, editable=False, on_delete=models.CASCADE)
  FK_ordenes = models.ForeignKey(Ordenes, null = True, editable=False, on_delete=models.CASCADE)
  FK_medico = models.ForeignKey(Medico, null = True, editable=False, on_delete=models.CASCADE)
    

class Interaccion(models.Model):
#   id_interaccion = models.AutoField(primary_key=True)
  descripcion_mensaje = models.CharField(max_length = 500)
  fecha = models.DateField()
  FK_paciente = models.ForeignKey(Paciente, null = True, editable=False, on_delete=models.CASCADE)
  FK_medico = models.ForeignKey(Medico, null = True, editable=False, on_delete=models.CASCADE)



