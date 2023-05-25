from django.shortcuts import render,redirect
from veterinariaApp.controllers.AdminitradorController.AdministradorInputs import afiliarPersona
from veterinariaApp.controllers.auth import autenticar
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError



def iniciar(request):
    return render(request, 'shared/index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'shared/register.html')
    else:

     if request.POST["password1"] == request.POST["password2"]:
        try:
          usuario = request.POST["username"]
          cedula = request.POST["cedula"]
          nombre = request.POST["nombre"]
          edad = request.POST["edad"]
          rol = request.POST["rol"]
          contraseña = request.POST["password1"]
          user=afiliarPersona(nombre, cedula, edad, rol, usuario,contraseña)
          if user is None:
            return render(request, 'shared/register.html',{"error":"Usuario ya existe"})
          else:
           return render(request,'shared/admin.html')
        except IntegrityError as e:
           return render(request, 'shared/register.html',{"error":e.args})
     else:
         return render(request, 'shared/register.html',{"error":"Las contraseñas no coinciden"})
     
def singup(request):
    if request.method == 'GET':
        return render(request, 'shared/singup.html',{"url":" "})
    else:
       try:
        usuario = request.POST["user"]
        contraseña = request.POST["pass"]
        log=autenticar(usuario,contraseña)
        if log is not None:
         request.session['username'] = log.nombreUsuario
         return render(request, 'shared/admin.html',{"url":"administrator/"})
        
        else:
          return render(request, 'shared/singup.html',{"url":" ","error":"Usuario o contraseña incorrectos"})
       except IntegrityError as e: 
        return render(request, 'shared/singup.html',{"error":e.args})

    
    
def administrator(request):
       username = request.session.get('username')
       if username:
        return render(request, 'shared/admin.html')
       else:
          return render(request, 'shared/index.html',{"error":"debe estar autenticado"})

def logout(request):
   request.session['username'] =None
   return render(request,'shared/index.html',{"error":"session cerrada"})