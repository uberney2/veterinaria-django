from veterinariaApp.controllers.AdminitradorController.AdministradorBussines import addEmpleado
from django.core import signing


def afiliarPersona(nombre, cedula, edad, rol, usuario, contraseña):
    
    if usuario == None or usuario == "":
        raise Exception("ususario invalido")
        return
    try:
        cedula = int(cedula)
    except:
        raise Exception("cedula invalida")
        return
    if nombre == None or nombre == "":
         raise Exception("ususario invalido")
         return
    try:
        edad = int(edad)
    except:
        raise Exception("edad invalida")
        return
    if rol == None or rol == "": 
        raise Exception("rol invalido")
        return
    roles = {
    "Administrador": 1,
    "Veterinario": 2,
    "Vendedor": 3,
    "Dueño de mascota": 4
}
    Rol = roles.get(rol)
    encrypted_pass = signing.dumps(contraseña)
    user=addEmpleado(nombre, cedula, edad, Rol, usuario, encrypted_pass)
    print(user)
    return user
    
