from veterinariaApp.controllers.VendedorController.VendedorControllerBusiness import buscar,buscarOrdenbyId


def BuscarDueño(cedula_dueño):
    if cedula_dueño == None or cedula_dueño == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedula = int(cedula_dueño)
    except:
        print("la cedula debe ser numerica")
    return buscar(cedula_dueño)

def buscarOrdenes(cedula):
    return buscarOrdenbyId(cedula)

