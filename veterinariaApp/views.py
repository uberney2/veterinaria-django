import json
from django.shortcuts import render,redirect
from veterinariaApp.controllers.AdminitradorController.AdministradorInputs import afiliarPersona
from veterinariaApp.controllers.VeterinarioController.veterinarioControllerInputs import AgregarDueñoMascota, AgregarMascota, CreacionHistoriaClinica
from veterinariaApp.controllers.auth import autenticar
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from veterinariaApp.forms import CrearFormHistoriaClinica, AgregarDueñoMascotaForm, AgregarMascotaForm
from veterinariaApp.models import HistoriaClinica
from .conexionMongoDB import collection



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

def crearHistoriaClinica(request):
    if request.method == 'GET':
        return render(request, 'historia-clinica/historia_clinica.html',{
            'form': CrearFormHistoriaClinica()
        })
    else:
        medicoVeterinario = request.POST['medicoVeterinario']
        motivoConsulta= request.POST['motivoConsulta']
        sintomatologia= request.POST['sintomatologia']
        diagnostico= request.POST['diagnostico']
        procedimiento= request.POST['procedimiento']
        medicamento= request.POST['medicamento']
        dosis= request.POST['dosis']
        idOrden= request.POST['idOrden']
        historialVacunacion= request.POST['historialVacunacion']
        alergiasMedicamentos= request.POST['alergiasMedicamentos']
        detalleProcedimiento =request.POST['detalleProcedimiento']
        estadoOrden =request.POST['estadoOrden']
        
        CreacionHistoriaClinica(medicoVeterinario, motivoConsulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, idOrden, estadoOrden, historialVacunacion, alergiasMedicamentos, detalleProcedimiento )
        
        return redirect('hc')
    
def crearDueñoMascota(request):
    if request.method == 'GET':
        print("entre")
        return render(request, 'historia-clinica/registro_dueño_mascota.html',{
            'form': AgregarDueñoMascotaForm()
        })
    else:
        cedula = request.POST['cedula']
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        AgregarDueñoMascota(cedula, nombre, edad )
        return redirect('dueño')
    
def crearMascota(request):
    if request.method == 'GET':
        print("entre")
        return render(request, 'historia-clinica/agregar-mascota.html',{
            'form': AgregarMascotaForm()
        })
    else:
        nombre = request.POST['nombre']
        cedula_dueño = request.POST['cedula_dueño']
        edad = request.POST['edad']
        especie = request.POST['especie']
        raza = request.POST['raza']
        caracteristicas = request.POST['caracteristicas']
        peso = request.POST['peso']
        AgregarMascota(nombre, cedula_dueño, edad, especie, raza, caracteristicas, peso)
        return redirect('mascota')