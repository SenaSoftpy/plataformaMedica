from django.shortcuts import render





def inicio(request):
  
    return render(request, 'index.html')

def login_usuario(request):

    return render(request, 'login.html')

def registro_usuario(request):

    return render(request, 'login.html')

def cerrar_sesion(request):

    return render(request, 'login.html')
