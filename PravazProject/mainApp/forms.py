from django import forms
from .models import Paciente

class FormularioRegistro:
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellidos', 'telefono', 'correo', 'fecha_nacimiento', 'contraseña'] 
