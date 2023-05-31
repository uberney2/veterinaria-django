import json
from django.shortcuts import render, redirect
from veterinariaApp.controllers.AdminitradorController.AdministradorInputs import afiliarPersona
from veterinariaApp.controllers.AdminitradorController.AdministradorBussines import lookAll
from veterinariaApp.controllers.VeterinarioController.veterinarioControllerInputs import AgregarDueñoMascota, AgregarMascota, CreacionHistoriaClinica, BuscarDueño, buscarMascota, BuscarHistoriasbyId, consultarHistoriaClinicaByFecha, updateHistoriaClinica, buscarOrdenes, cancelarOrdenes, buscarFactura, BuscarFacturasbyId
from veterinariaApp.controllers.auth import autenticar
from veterinariaApp.controllers.VendedorController.VendedorControllerBusiness import VentaOrden, VentaSinOrden,VentaConOrden
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from veterinariaApp.forms import BuscarUsuarioForm, CrearFormHistoriaClinica, AgregarDueñoMascotaForm, AgregarMascotaForm, comenzarCreaciónHistoriaClinicaForm
from veterinariaApp.models import HistoriaClinica, Usuario
from .conexionMongoDB import collection
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist



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
                user = afiliarPersona(
                    nombre, cedula, edad, rol, usuario, contraseña)
                if user is None:
                    return render(request, 'shared/register.html', {"error": "Usuario ya existe"})
                else:
                    return render(request, 'shared/admin.html')
            except IntegrityError as e:
                return render(request, 'shared/register.html', {"error": e.args})
        else:
            return render(request, 'shared/register.html', {"error": "Las contraseñas no coinciden"})


def singup(request):
    if request.method == 'GET':
        return render(request, 'shared/singup.html', {"url": " "})
    else:
        try:
            usuario = request.POST["user"]
            contraseña = request.POST["pass"]
            log = autenticar(usuario, contraseña)
            if log is not None:
                request.session['username'] = log.nombreUsuario
                if log.rol_id == "1":
                    return redirect('admin')
                elif log.rol_id == "2":
                    return redirect('veterinario')
                else:
                    return redirect('vendedor')

            else:
                return render(request, 'shared/singup.html', {"url": " ", "error": "Usuario o contraseña incorrectos"})
        except IntegrityError as e:
            return render(request, 'shared/singup.html', {"error": e.args})


def administrator(request):
    username = request.session.get('username')
    if username:
        users = lookAll()
        return render(request, 'shared/admin.html', {'users': users})
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})


def logout(request):
    request.session['username'] = None
    return render(request, 'shared/error.html', {"error": "session cerrada"})


def crearHistoriaClinica(request, id):
    username = request.session.get('username')
    if username:
        print(id)
        if request.method == 'GET':
            return render(request, 'historia-clinica/historia_clinica.html', {
                'form': CrearFormHistoriaClinica(),
                'id': id,
            })
        else:
            motivoConsulta = request.POST['motivoConsulta']
            sintomatologia = request.POST['sintomatologia']
            diagnostico = request.POST['diagnostico']
            procedimiento = request.POST['procedimiento']
            medicamento = request.POST['medicamento']
            dosis = request.POST['dosis']
            historialVacunacion = request.POST['historialVacunacion']
            alergiasMedicamentos = request.POST['alergiasMedicamentos']
            detalleProcedimiento = request.POST['detalleProcedimiento']

            CreacionHistoriaClinica(id, username, motivoConsulta, sintomatologia, diagnostico, procedimiento,
                                    medicamento, dosis, historialVacunacion, alergiasMedicamentos, detalleProcedimiento)

            return redirect('veterinario')
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})


def crearDueñoMascota(request):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            return render(request, 'historia-clinica/registro_dueño_mascota.html', {
                'form': AgregarDueñoMascotaForm()
            })
        else:
            cedula = request.POST['cedula']
            nombre = request.POST['nombre']
            edad = request.POST['edad']
            AgregarDueñoMascota(cedula, nombre, edad)
            return redirect('veterinario')
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})


def crearMascota(request):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            return render(request, 'historia-clinica/agregar-mascota.html', {
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
            AgregarMascota(nombre, cedula_dueño, edad, especie,
                           raza, caracteristicas, peso)
            return redirect('veterinario')
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})


def eliminarUser(request, user_id):
    user = get_object_or_404(Usuario, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return render(request, 'shared/admin.html', {"error": "eliminado, Actualice por favor"})
    return render(request, 'shared/admin.html', {"error": "No pudo ser eliminado "})


def vendedor(request):
    username = request.session.get('username')
    if username:
        return render(request, 'medicamento/vendedor.html')
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})


def ventaSinOrden(request):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            return render(request, 'medicamento/ventaSinOrden.html')
        elif request.method == 'POST':
            cedulaDueño = request.POST["cedulaDueño"]
            productos = [valor.strip() for valor in request.POST["productos"].split(",")]
            cantidad = request.POST["cantidad"]
            total = request.POST["total"]
            VentaSinOrden(cedulaDueño, productos, cantidad, total)
        
    return redirect('ventaSinOrden')


def ventaConOrden(request,id):
    username = request.session.get('username')
    if username:
        idMascota = request.GET.get('idMascota')
        if request.method == 'GET':
            return render(request, 'medicamento/ventaConOrden.html', {
                    'idOrden': id,
                    'idMascota': idMascota
                })
        elif request.method == 'POST':
            cedulaDueño = request.POST["cedulaDueño"]
            productos = [valor.strip() for valor in request.POST["productos"].split(",")]
            cantidad = request.POST["cantidad"]
            total = request.POST["total"]
            idMascota = request.POST["idMascota"]
            IdOrden = request.POST["idOrden"]
            VentaConOrden(cedulaDueño, productos, cantidad, total,idMascota,IdOrden)
            
    return redirect('vendedor')


def indexHistoriaClinica(request):
    username = request.session.get('username')
    if username:
        return render(request, 'historia-clinica/indexVeterinario.html')
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})


def desarrolloHistoriaClinica(request):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            return render(request, 'historia-clinica/comienzo_hc.html', {
                'form': BuscarUsuarioForm(),
                'disableBuscarUsuario': False
            })
        else:
            cedula_dueño = request.POST['cedula_dueño']
            dueño = BuscarDueño(cedula_dueño)
            if dueño is None:
                return render(request, 'historia-clinica/comienzo_hc.html', {
                    'form': BuscarUsuarioForm(),
                    'hasDueño': False,
                    'disableBuscarUsuario': True
                })
            else:
                mascotas = buscarMascota(dueño.id)
                if mascotas is None:
                    return render(request, 'historia-clinica/comienzo_hc.html', {
                        'form': BuscarUsuarioForm(),
                        'hasDueño': True,
                        'mascotas': None,
                        'disableBuscarUsuario': True
                    })
                else:
                    return render(request, 'historia-clinica/comienzo_hc.html', {
                        'form': BuscarUsuarioForm(),
                        'formMascota': comenzarCreaciónHistoriaClinicaForm(),
                        'hasDueño': True,
                        'mascotas': mascotas,
                        'disableBuscarUsuario': True,
                    })

    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})


def editarHistoriaClinica(request):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            return render(request, 'historia-clinica/comienzo_edicion.html', {
                'form': BuscarUsuarioForm(),
                'disableBuscarUsuario': False
            })
        else:
            cedula_dueño = request.POST['cedula_dueño']
            dueño = BuscarDueño(cedula_dueño)
            if dueño is None:
                return render(request, 'historia-clinica/comienzo_edicion.html', {
                    'hasDueño': False,
                    'disableBuscarUsuario': True
                })
            else:
                mascotas = buscarMascota(dueño.id)
                if mascotas is None:
                    return render(request, 'historia-clinica/comienzo_edicion.html', {
                        'hasDueño': True,
                        'mascotas': None,
                        'disableBuscarUsuario': True
                    })
                else:
                    return render(request, 'historia-clinica/comienzo_edicion.html', {
                        'hasDueño': True,
                        'mascotas': mascotas,
                        'disableBuscarUsuario': True
                    })
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})

def listarHistoriaClinica(request, id):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            historiasClinicas = BuscarHistoriasbyId(id)
            print(historiasClinicas)
            return render(request, 'historia-clinica/ver_historias_clinicas.html', {
                'form': BuscarUsuarioForm(),
                'disableBuscarUsuario': False,
                'historias': historiasClinicas
            })
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})


def edicionHistoriaClinica(request, id):
    username = request.session.get('username')
    if username:
        fecha = request.GET.get('fecha')
        historiaClinica = consultarHistoriaClinicaByFecha(fecha, id)
        if request.method == 'GET':
            hc = historiaClinica.get(id, {}).get(fecha, None)
            return render(request, 'historia-clinica/editar_historia_clinica.html', {
                'form': BuscarUsuarioForm(),
                'disableBuscarUsuario': False,
                'hc': hc,
                'id': id,
                'fecha': fecha
            })
        else:
            fecha = request.POST['fecha']
            medicoVeterinario = request.POST['medicoVeterinario']
            motivoConsulta = request.POST['motivoConsulta']
            sintomatologia = request.POST['sintomatologia']
            diagnostico = request.POST['diagnostico']
            procedimiento = request.POST['procedimiento']
            medicamento = request.POST['medicamento']
            dosis = request.POST['dosis']
            idOrden = request.POST['idOrden']
            historialVacunacion = request.POST['historialVacunacion']
            alergiasMedicamentos = request.POST['alergiasMedicamentos']
            detalleProcedimiento = request.POST['detalleProcedimiento']
            estadoOrden = request.POST['estadoOrden']
            updateHistoriaClinica(id, fecha, medicoVeterinario, motivoConsulta, sintomatologia, diagnostico, procedimiento,
                                  medicamento, dosis, idOrden, estadoOrden, historialVacunacion, alergiasMedicamentos, detalleProcedimiento)
            return redirect('veterinario')
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})


def cancelarOrden(request):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            return render(request, 'historia-clinica/cancelar-orden.html', {
                'form': BuscarUsuarioForm(),
                'disableBuscarUsuario': False,
            })
        else:
            cedula_dueño = request.POST['cedula_dueño']
            dueño = BuscarDueño(cedula_dueño)
            if dueño is None:
                return render(request, 'historia-clinica/cancelar-orden.html', {
                    'hasDueño': False,
                    'disableBuscarUsuario': True
                })
            else:
                ordenes = buscarOrdenes(cedula_dueño)
                if ordenes is None:
                    return render(request, 'historia-clinica/cancelar-orden.html', {
                        'hasDueño': True,
                        'ordenes': None,
                        'disableBuscarUsuario': True
                    })
                else:
                    return render(request, 'historia-clinica/cancelar-orden.html', {
                        'hasDueño': True,
                        'ordenes': ordenes,
                        'disableBuscarUsuario': True
                    })
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})


def confirmacionCancelacionOrden(request, id):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            fecha = request.GET.get('fecha')
            idMascota = request.GET.get('idMascota')
            cencelacion = cancelarOrdenes(id, fecha, idMascota)
            return render(request, 'historia-clinica/cancelar-orden.html', {
                'form': BuscarUsuarioForm(),
                'disableBuscarUsuario': False,
            })
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})


def eliminarUser(request, user_id):
    try:
        user = Usuario.objects.using('mysql').get(pk=user_id)
        if request.method == 'POST':
            user.delete()
            return render(request, 'shared/admin.html', {"error": "Eliminado. Por favor, actualice la página."})
        return render(request, 'shared/admin.html', {"error": "No se pudo eliminar."})
    except ObjectDoesNotExist:
        return render(request, 'shared/admin.html', {"error": "El usuario no existe."})
    
def comienzoBuscarFacturas(request):
    print('entre')
    username = request.session.get('username')
    if username:
        
        if request.method == 'GET':
            return render(request, 'factura/comienzo_factura.html', {
                'form': BuscarUsuarioForm(),
                'disableBuscarUsuario': False,
            })
        else:
            cedula_dueño = request.POST['cedula_dueño']
            dueño = BuscarDueño(cedula_dueño)
            if dueño is None:
                return render(request, 'factura/comienzo_factura.html', {
                    'hasDueño': False,
                    'disableBuscarUsuario': True
                })
            else:
                facturas = buscarFactura(dueño.cedula)
                if facturas is None:
                    return render(request, 'factura/comienzo_factura.html', {
                        'hasDueño': True,
                        'facturas': None,
                        'disableBuscarUsuario': True
                    })
                else:
                    return render(request, 'factura/comienzo_factura.html', {
                        'hasDueño': True,
                        'facturas': facturas,
                        'disableBuscarUsuario': True
                    })
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})
    
def listarFacturas(request, id):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            facturas = BuscarFacturasbyId(id)
            return render(request, 'factura/ver_facturas.html', {
                'facturas': facturas
            })
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})

def comienzo_factura(request):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            return render(request, 'medicamento/comienzo_factura.html', {
                    'form': BuscarUsuarioForm(),
                    'disableBuscarUsuario': False
                })
        else:
            cedula_dueño = request.POST['cedula_dueño']
            dueño = BuscarDueño(cedula_dueño)
            if dueño is None:
                return render(request, 'medicamento/comienzo_factura.html', {
                    'hasDueño': False,
                    'disableBuscarUsuario': True
                })
            else:
                ordenes = buscarOrdenes(dueño.cedula)
                if ordenes is None:
                    return render(request, 'medicamento/comienzo_factura.html', {
                        'hasDueño': True,
                        'ordenes': None,
                        'disableBuscarUsuario': True
                    })
                else:
                    return render(request, 'medicamento/comienzo_factura.html', {
                        'hasDueño': True,
                        'ordenes': ordenes,
                        'disableBuscarUsuario': True
                    })
    else:
        return render(request, 'shared/error.html', {"error": "debe estar autenticado"})
    
