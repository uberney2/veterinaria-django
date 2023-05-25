import uuid
from veterinariaApp.Enums.rolesEnum import Roles
from veterinariaApp.models import Mascota, Rol, Usuario
from django.core.exceptions import ObjectDoesNotExist

def buscar(cedula):
    try:
        usuario_existente = Usuario.objects.using('mysql').get(cedula=str(cedula))
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


def afiliarMascota(nombre, cedula_dueño, edad, especie, raza, caracteristicas, peso):
    personaEncontrada = buscar(cedula_dueño)
    if personaEncontrada is None:
        return None

    id = uuid.uuid4()
    Mascota.objects.using('mysql').create(id=id, nombre=nombre, cedula_dueño=cedula_dueño, edad=edad, especie=especie, raza=raza, caracteristicas=caracteristicas, peso=peso, Usuario = personaEncontrada)
    return 