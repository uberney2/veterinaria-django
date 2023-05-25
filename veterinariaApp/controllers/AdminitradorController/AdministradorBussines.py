from veterinariaApp.models import Usuario,Roles
import uuid
from django.core.exceptions import ObjectDoesNotExist
def buscar(usuario):
    try:
        usuario_existente = Usuario.objects.get(nombreUsuario=usuario)
        return usuario_existente
    except ObjectDoesNotExist:
        return None

def addEmpleado(nombre, cedula, edad, rol, usuario, contraseña):
    usuario_existe = buscar(usuario)
    if usuario_existe is not None:
        return None
    else:
        id = uuid.uuid4()
        rol_objeto = Roles.objects.get(id=rol)
        nuevo_usuario = Usuario.objects.create(
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
    

   