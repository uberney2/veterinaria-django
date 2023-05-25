import uuid
from veterinariaApp.Enums.rolesEnum import Roles
from veterinariaApp.models import Rol, Usuario
from django.core.exceptions import ObjectDoesNotExist

def buscar(cedula):
    try:
        usuario_existente = Usuario.objects.get(cedula=cedula)
        return usuario_existente
    except ObjectDoesNotExist:
        return None

def AfiliarDueñoMascota(nombre,cedula,edad):
    usuario_existe = buscar(cedula)
    if usuario_existe is not None:
        return None
    else:
        id = uuid.uuid4()
        rol_dueño_mascota, created = Rol.objects.get_or_create(id=4)
        Usuario.objects.using('mysql').create(id=id, nombre=nombre, cedula=cedula, edad=edad, rol=rol_dueño_mascota)
        return