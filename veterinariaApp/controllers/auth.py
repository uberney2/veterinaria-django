from veterinariaApp.models import Usuario
from django.core.exceptions import ObjectDoesNotExist
from django.core import signing
from django.contrib.auth import authenticate

def buscar(usuario):
    try:
        usuario_existente = Usuario.objects.get(nombreUsuario=usuario)
        return usuario_existente
    except ObjectDoesNotExist:
        return None

def autenticar(usuario, contraseña):
    usuario_existe = buscar(usuario)
    if usuario_existe is not None:
        contraseña_desencriptada = signing.loads(usuario_existe.Contraseña)  
        if contraseña_desencriptada == contraseña:
            return usuario_existe
        else:
            return None
    else:
        return None
