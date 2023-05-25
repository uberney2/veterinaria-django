from veterinariaApp.controllers.VeterinarioController.veterinarioControllerBussines import HistoriaClinicaCreacion, AfiliarDueñoMascota, afiliarMascota


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
    
def AgregarMascota(nombre, cedulaDueño, edad, especie, raza, caracteristicas, peso):

    if nombre == None or nombre == " ":
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
    
    if especie == None or especie == " ":
        print("la especie no puede ser un espacio vacia")
        return
    
    if raza == None or raza == " ":
        print("la raza no puede ser un espacio vacia")
        return
    
    if caracteristicas == None or caracteristicas == " ":
        print("las caracteristicas no pueden ser un espacio vacio")
        return
    
    if peso == None or peso == " ":
        print("el peso no puede ser un espacio vacio")
        return
    try:
        peso = int(peso)
    except:
        print("el peso debe ser numerica")
        return
    
    print("------------validacion exitosa---------------------")
    mascota = afiliarMascota(nombre, cedula, edad, especie, raza, caracteristicas, peso)
    
    return

def CreacionHistoriaClinica(profesionalAtiende, motivoConsulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, idOrden, estadoOrden, vacunas, alergiaMedicamentos, detalleProcedimiento ):
    if motivoConsulta == None or motivoConsulta == " ":
        print("Motivo onsulta no pueden ser un espacio vacio")
        return
    
    if sintomatologia == None or sintomatologia == " ":
        print("sintomatologia no pueden ser un espacio vacio")
        return
    
    if diagnostico == None or diagnostico == " ":
        print("diagnostico no pueden ser un espacio vacio")
        return
    
    if procedimiento == None or procedimiento == " ":
        print("procedimiento no pueden ser un espacio vacio")
        return
    
    if alergiaMedicamentos == None or alergiaMedicamentos == " ":
        print("Alergia medicamentos no pueden ser un espacio vacio")
        return
    
    if detalleProcedimiento == None or detalleProcedimiento == " ":
        print("Detalle procedimiento no pueden ser un espacio vacio")
        return
    
    HistoriaClinicaCreacion(profesionalAtiende, motivoConsulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, idOrden, estadoOrden, vacunas, alergiaMedicamentos, detalleProcedimiento )