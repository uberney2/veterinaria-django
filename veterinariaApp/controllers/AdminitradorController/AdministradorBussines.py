from veterinariaApp.models import Usuario,Rol
import uuid
from django.core.exceptions import ObjectDoesNotExist
def buscar(usuario):
    try:
        usuario_existente = Usuario.objects.using('mysql').get(nombreUsuario=usuario)
        return usuario_existente
    except ObjectDoesNotExist:
        return None

def addEmpleado(nombre, cedula, edad, rol, usuario, contraseña):
    usuario_existe = buscar(usuario)
    if usuario_existe is not None:
        return None
    else:
        id = uuid.uuid4()
        rol_objeto = Rol.objects.get(id=rol)
        nuevo_usuario = Usuario.objects.using('mysql').create(
            id=id,
            nombreUsuario=usuario,
            Contraseña=contraseña,
            cedula=cedula,
            nombre=nombre,
            edad=edad,
            rol= rol_objeto
        )
        nuevo_usuario.save()
        return nuevo_usuario
   
Roles = {
        "1": "Administrador",
        "2": "Veterinario",
        "3": "Vendedor",
        "4": "Dueño de mascota"
    }
def lookAll():
    
    users = Usuario.objects.using('mysql').all()

    for user in users:
         rol = user.rol_id
         user.rol_id = Roles.get(rol)

    return users
