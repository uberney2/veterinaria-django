import uuid
from veterinariaApp.Enums.rolesEnum import Roles
from veterinariaApp.models import HistoriaClinica, Mascota, OrdenMascotas, Rol, Usuario
from django.core.exceptions import ObjectDoesNotExist
from veterinariaApp.conexionMongoDB import collection
from datetime import datetime

def buscar(cedula):
    try:
        usuario_existente = Usuario.objects.using('mysql').get(cedula=str(cedula))
        return usuario_existente
    except ObjectDoesNotExist:
        return None

def buscarMascotas(cedulaDueño):
    try:
        mascotas = Mascota.objects.using('mysql').filter(Usuario=str(cedulaDueño))
        return mascotas
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

def buscarHistoriaClinica(id):
    return collection.find_one(id)
    

def HistoriaClinicaCreacion(id, username, motivoConsulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, vacunas, alergiaMedicamentos, detalleProcedimiento ):
    idOrden = f'{uuid.uuid4()}'
    orden = OrdenMascotas()
    profesionalAtiende = Usuario.objects.using('mysql').get(nombreUsuario = username).nombre
    if medicamento != "ninguno":
        mascota = Mascota.objects.using('mysql').get(id=str(id))
        usuario = Usuario.objects.using('mysql').get(id=str(mascota.Usuario.id))
        orden.id = idOrden
        orden.idMascota = id
        orden.cedulaDueno = usuario.cedula
        orden.cedulaVeterinario = "1037238472"
        orden.nombreMedicamento = medicamento
        orden.estado = "Activa"
        estadoOrden = "Activa"
        aplicaOrden = True
    else:
        idOrden = 'no aplica'
        estadoOrden = "No aplica"
        aplicaOrden = False
    try:
        hasHistoriaClinica = buscarHistoriaClinica(id)
    except HistoriaClinica.DoesNotExist:
        hasHistoriaClinica = None
    if hasHistoriaClinica is None:
        fechaConsulta = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        hcJson = {}
        hcJson['_id'] = id  
        hcJson[id ] = {}  
        hcJson[id ][fechaConsulta] = {
            "medicoVeterinario": profesionalAtiende,
            "motivoConsulta": motivoConsulta,
            "sintomatologia": sintomatologia,
            "diagnostico": diagnostico,
            "procedimiento": procedimiento,
            "medicamento": medicamento,
            "dosis": dosis,
            "idOrden": idOrden,
            "historialVacunacion": vacunas,
            "alergiasMedicamentos": alergiaMedicamentos,
            "detalleProcedimiento": detalleProcedimiento,
            "estadoOrden": estadoOrden
        }
        collection.insert_one(hcJson)
        
        if aplicaOrden == True:
            orden.fechaHistoria = fechaConsulta
            OrdenMascotas.objects.using('mysql').create(id=orden.id, idMascota = orden.idMascota, cedulaDueno = orden.cedulaDueno, cedulaVeterinario = orden.cedulaVeterinario, nombreMedicamento = orden.nombreMedicamento, fechaHistoria = orden.fechaHistoria, estado = orden.estado )
            
    else:
        fechaConsulta = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        nuevaInfo = {
            "medicoVeterinario": profesionalAtiende,
            "motivoConsulta": motivoConsulta,
            "sintomatologia": sintomatologia,
            "diagnostico": diagnostico,
            "procedimiento": procedimiento,
            "medicamento": medicamento,
            "dosis": dosis,
            "idOrden": idOrden,
            "historialVacunacion": vacunas,
            "alergiasMedicamentos": alergiaMedicamentos,
            "detalleProcedimiento": detalleProcedimiento,
            "estadoOrden": estadoOrden
        }
        
        hasHistoriaClinica[id][fechaConsulta]=nuevaInfo
        collection.update_one({'_id': id} , {'$set': hasHistoriaClinica})
        if aplicaOrden == True:
            orden.fechaHistoria = fechaConsulta
            OrdenMascotas.objects.using('mysql').create(id=orden.id, idMascota = orden.idMascota, cedulaDueno = orden.cedulaDueno, cedulaVeterinario = orden.cedulaVeterinario, nombreMedicamento = orden.nombreMedicamento, fechaHistoria = orden.fechaHistoria, estado = orden.estado  )

def buscarHistoriasClinicasById(id):
    return buscarHistoriaClinica(id)

def consultarHistoriaClinicaByFechaAndId(fecha, id):
    filtro = {'_id': id, f'{id}.{fecha}': {'$exists': True}}
    projection = {f'{id}.{fecha}': 1, '_id': 0}
    hc = collection.find_one(filtro, projection)
    try:
        return hc
        # motivo_consulta = registro[fecha]['motivoConsulta']
    except ObjectDoesNotExist:
        return None

def actualizarHistoriaClinica(id, fecha, medicoVeterinario, motivoConsulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, idOrden, estadoOrden, historialVacunacion, alergiasMedicamentos, detalleProcedimiento ):
    hc = collection.find_one({"_id": id})
    nuevaInfo = {
            "medicoVeterinario": medicoVeterinario,
            "motivoConsulta": motivoConsulta,
            "sintomatologia": sintomatologia,
            "diagnostico": diagnostico,
            "procedimiento": procedimiento,
            "medicamento": medicamento,
            "dosis": dosis,
            "idOrden": idOrden,
            "historialVacunacion": historialVacunacion,
            "alergiasMedicamentos": alergiasMedicamentos,
            "detalleProcedimiento": detalleProcedimiento,
            "estadoOrden": estadoOrden
        }
    hc[str(id)][fecha].update(nuevaInfo)
    collection.update_one({"_id": id}, {"$set": hc})

def buscarOrdenesById(cedula):
    ordenes = OrdenMascotas.objects.using('mysql').filter(cedulaDueno=str(cedula))  
    return ordenes

def cancelacionOrden(idOrden, fecha, idMascota):
    orden = OrdenMascotas.objects.using('mysql').get(id = idOrden)
    orden.estado = "Cancelado"
    orden.save()
    
    filter = {
        "_id": idMascota,
        f"{idMascota}.{fecha}.idOrden": idOrden
    }
    update = {
        "$set": {
            f"{idMascota}.{fecha}.estadoOrden": "Cancelada"
        }
    }
    collection.update_one(filter, update)
    return True
