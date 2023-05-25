from veterinariaApp.controllers.VeterinarioController.veterinarioControllerBussines import AfiliarDueñoMascota


def AgregarDueñoMascota(cedulaDueño, nombreDueño, edad):
    if nombreDueño == None or nombreDueño == " ":
        print("el nombre no puede ser un espacio vacio")
        return
    
    if cedulaDueño == None or cedulaDueño == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedula = int(cedulaDueño)
    except:
        print("la cedula debe ser numerica")
        return
    if edad == None or edad == " ":
        print("la edad no puede ser un espacio vacio")
        return
    try:
        edad = int(edad)
    except:
        print("la edad debe ser numerica")
        return
    print("------------validacion exitosa---------------------")
    AfiliarDueñoMascota(nombreDueño, cedula, edad)