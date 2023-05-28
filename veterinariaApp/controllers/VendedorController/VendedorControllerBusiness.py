import uuid
from veterinariaApp.Enums.rolesEnum import Roles
from veterinariaApp.models import  Usuario, Factura, Productos
from django.core.exceptions import ObjectDoesNotExist
from veterinariaApp.conexionMongoDB import collection
from datetime import datetime

def buscar(cedula):
    try:
        usuario_existente = Usuario.objects.using('mysql').get(cedula=str(cedula))
        return usuario_existente
    except ObjectDoesNotExist:
        return None
    
def VentaOrden(cedula,medicamentos,cantidad,valor):
    try:
        productos=Productos.objects.using('mysql').create(cedula_comprador=cedula,medicamento=medicamentos,cantidad=cantidad,valor_venta=valor)
        productos.save()
        return productos
    except ObjectDoesNotExist:
        return None    


