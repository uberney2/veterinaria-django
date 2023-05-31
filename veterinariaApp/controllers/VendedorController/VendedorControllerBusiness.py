import uuid
from veterinariaApp.Enums.rolesEnum import Roles
from veterinariaApp.models import  Usuario, Factura, Productos,OrdenMascotas
from django.core.exceptions import ObjectDoesNotExist
from veterinariaApp.conexionMongoDB import collection
from datetime import datetime

def buscar(cedula):
    try:
        usuario_existente = Usuario.objects.using('mysql').get(cedula=str(cedula))
        return usuario_existente
    except ObjectDoesNotExist:
        return None
    
def VentaOrden(id,idMascota,cedulaDueño,idOrden,productos,cantidad,total,fecha):
    try:
        id=uuid.uuid4()
        fecha=str(datetime)
        factura=Factura.objects.using('mysql').create(id=id,idMascota=idMascota,cedulaDueño=cedulaDueño,idOrden=idOrden,productos=productos,cantidad=cantidad,total=total,fecha=fecha)
        factura.save()
        return factura
    except ObjectDoesNotExist:
        return None    
    
def VentaSinOrden(cedulaDueño, productos, cantidad, total):
    try:
        id=str(uuid.uuid4())
        fecha=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        factura=Factura.objects.using('mysql').create(id=id,cedulaDueño=cedulaDueño,productos=productos,cantidad=cantidad,total=total,fecha=fecha)
        factura.save()
        return factura
    except ObjectDoesNotExist:
        return None  
    
def VentaConOrden(cedulaDueño, productos, cantidad, total,identificacionMascota,identificacionOrden):
    try:
        id=str(uuid.uuid4())
        idMascota=identificacionMascota
        idOrden=identificacionOrden
        fecha=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        factura=Factura.objects.using('mysql').create(id=id,idMascota=idMascota,idOrden=idOrden,cedulaDueño=cedulaDueño,productos=productos,cantidad=cantidad,total=total,fecha=fecha)
        factura.save()
        return factura
    except ObjectDoesNotExist:
        return None 
    
def buscarOrdenbyId(cedula):
    try:
        usuario_existente = Usuario.objects.using('mysql').get(cedula=str(cedula))
        return usuario_existente
    except ObjectDoesNotExist:
        return None

