from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Importamos nuestro modelo de formulario
from .forms import FormularioRegistro
#  son necesarios para el inicio de sesion
from django.contrib.auth import authenticate, login, logout 




def inicio(request):

    
  
    return render(request, 'index.html', {
        'titulo': 'Hola'
    })

def login_pagina(request):
    # Verificamos si esta autenticado, en caso contrario mostramos el formulario de registro
    if request.user.is_authenticated: 
        return ('index')
    else:
        if request.method == 'POST':
            usuario = request.POST.get('usuario') # recogemos el dato que nos llega en el name de los campos del formulario
            contrasena = request.POST.get('contrasena')

            usuario = authenticate(request, usuario=usuario, contrasena=contrasena)

            if usuario is not None:
                # Le pasamos el usuario a identificar
                login(request, user) 
                return redirect('index')
            else:
                #mensajes flash
                messages.warning(request, 'Credenciales incorrectas')

        return render(request, 'usuarios/login.html')

# Registro del Usuario
def registro_pagina(request):

    # Verificamos si esta autenticado
    if request.usuario.is_authenticated:    
        return ('inicio')
    else:
        # Creamos nuestro formulario
        formulario_registro = FormularioRegistro() 

        if request.method == 'POST':
            # Guardamos los datos recividos.
            formulario_registro = FormularioRegistro(request.POST) 

            if formulario_registro.is_valid():
                formulario_registro.save()
                messages.success(request, 'Te has registrado Correctamente')

                return redirect('index')

        context = {
            'title': 'Registro',
            'formulario_registro': formulario_registro
        }
        return render(request, 'usuario/registro.html', context)

    return render(request, 'registro.html')

# Cerramos Sesión
def cerrar_sesion(request):
    logout(request)
    return render(request, 'login.html')
