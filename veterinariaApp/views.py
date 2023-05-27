import json
from django.shortcuts import render,redirect
from veterinariaApp.controllers.AdminitradorController.AdministradorInputs import afiliarPersona
from veterinariaApp.controllers.AdminitradorController.AdministradorBussines import lookAll
from veterinariaApp.controllers.VeterinarioController.veterinarioControllerInputs import AgregarDueñoMascota, AgregarMascota
from veterinariaApp.controllers.auth import autenticar
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from veterinariaApp.forms import CrearFormHistoriaClinica, AgregarDueñoMascotaForm, AgregarMascotaForm
from veterinariaApp.models import HistoriaClinica,Usuario
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
           return redirect('admin')
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
         if log.rol_id=="1":
          return redirect('admin')
         elif log.rol_id=="4":
            return redirect('dueño')
        
        else:
          return render(request, 'shared/singup.html',{"url":" ","error":"Usuario o contraseña incorrectos"})
       except IntegrityError as e: 
        return render(request, 'shared/singup.html',{"error":e.args})

    
    
def administrator(request):
       username = request.session.get('username')
       if username: 
        users= lookAll()
        return render(request, 'shared/admin.html',{'users':users})
       else:
          return render(request, 'shared/error.html',{"error":"debe estar autenticado"})

def logout(request):
   request.session['username'] =None
   return render(request,'shared/error.html',{"error":"session cerrada"})

def crearHistoriaClinica(request):
     username = request.session.get('username')
     if username:
        if request.method == 'GET':
         return render(request, 'historia-clinica/historia_clinica.html',{
            'form': CrearFormHistoriaClinica()
        })
        else:
         hcJson = {}
         hcJson['_id'] = request.POST.get('_id', '')  # Acceder al campo _id usando request.POST.get()
         hcJson[request.POST.get('_id', '')] = {}  # Acceder al campo _id usando request.POST.get()
         hcJson[request.POST.get('_id', '')][request.POST['fechaConsulta']] = {
             "medicoVeterinario": request.POST['medicoVeterinario'],
             "motivoConsulta": request.POST['motivoConsulta'],
             "sintomatologia": request.POST['sintomatologia'],
             "diagnostico": request.POST['diagnostico'],
             "procedimiento": request.POST['procedimiento'],
             "medicamento": request.POST['medicamento'],
             "dosis": request.POST['dosis'],
             "idOrden": request.POST['idOrden'],
             "historialVacunacion": request.POST['historialVacunacion'],
             "alergiasMedicamentos": request.POST['alergiasMedicamentos'],
             "detalleProcedimiento": request.POST['detalleProcedimiento'],
             "estadoOrden": request.POST['estadoOrden']
         }
         print(hcJson)
         # hcJson.pop('_id', None)
         collection.insert_one(hcJson)
         # HistoriaClinica.objects.using('default').create(idMascota = hcJson['idMascota'], 
         #                                                 fechaConsulta=hcJson['fechaConsulta'],
         #                                                 medicoVeterinario=hcJson['medicoVeterinario'],
         #                                                 motivoConsulta=hcJson['motivoConsulta'],
         #                                                 sintomatologia=hcJson['sintomatologia'],
         #                                                 diagnostico=hcJson['diagnostico'],
         #                                                 procedimiento=hcJson['procedimiento'],
         #                                                 medicamento=hcJson['medicamento'],
         #                                                 dosis=hcJson['dosis'],
         #                                                 idOrden=hcJson['idOrden'],
         #                                                 historialVacunacion=hcJson['historialVacunacion'],
         #                                                 alergiasMedicamentos=hcJson['alergiasMedicamentos'],
         #                                                 detalleProcedimiento=hcJson['detalleProcedimiento'],
         #                                                 estadoOrden=hcJson['estadoOrden'])
         
         # HistoriaClinica.objects.using('default').create(hcJson)
         return redirect('hc')
     else:
        return render(request, 'shared/error.html',{"error":"debe estar autenticado"})

    
def crearDueñoMascota(request):
     username = request.session.get('username')
     if username:
        if request.method == 'GET':
         print("entre")
         return render(request, 'historia-clinica/registro_dueño_mascota.html',{
            'form': AgregarDueñoMascotaForm()})
        else:
         cedula = request.POST['cedula']
         nombre = request.POST['nombre']
         edad = request.POST['edad']
         AgregarDueñoMascota(cedula, nombre, edad )
         return redirect('dueño')
     else:
        return render(request, 'shared/error.html',{"error":"debe estar autenticado"})

    
    
def crearMascota(request):
    username = request.session.get('username')
    if username:
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
    else:
        return render(request, 'shared/error.html',{"error":"debe estar autenticado"})   
    
    
    

def eliminarUser(request,user_id):
   user = get_object_or_404(Usuario, pk=user_id)
   if request.method == 'POST':
    user.delete()
    return render(request,'shared/admin.html',{"error":"eliminado, Actualice por favor"})
   return render(request,'shared/admin.html',{"error":"No pudo ser eliminado "})