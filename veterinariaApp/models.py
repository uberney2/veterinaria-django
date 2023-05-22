from django.db import models

# Create your models here.

class HistoriaClinica(models.Model):
    idMascota = models.CharField(max_length=200)
    fechaConsulta = models.CharField(max_length=200)
    medicoVeterinario = models.CharField(max_length=200)
    motivoConsulta = models.CharField(max_length=200)
    medicamento = models.CharField(max_length=200)
    sintomatologia =  models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=200)
    procedimiento = models.CharField(max_length=200)
    medicamento = models.CharField(max_length=200)
    dosis = models.CharField(max_length=200)
    idOrden = models.CharField(max_length=200)
    historialVacunacion = models.CharField(max_length=200)
    alergiasMedicamentos = models.CharField(max_length=200)
    detalleProcedimiento = models.CharField(max_length=200)
    estadoOrden = models.BooleanField
    class Meta:
        app_label = 'veterinariaApp'
        db_table = 'Historia_clinica'


class Roles(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    descripcion = models.CharField(max_length=200)
    
    class Meta:
        app_label = 'veterinariaApp'
        db_table = 'Rol'

class Factura(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    idMascota = models.CharField(max_length=200)
    cedulaDueño = models.CharField(max_length=200)
    idOrden = models.CharField(max_length=200)
    productos = models.TextField
    total = models.TextField
    fecha = models.DateField
    
    class Meta:
        app_label = 'veterinariaApp'
        db_table = 'Factura'
        
class Usuario(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    nombreUsuario =  models.CharField(max_length=200)
    Contraseña =  models.CharField(max_length=200)
    cedula =  models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    edad = models.CharField(max_length=3)
    rol= models.ForeignKey(Roles, on_delete=models.PROTECT)
    Factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    class Meta:
        app_label = 'veterinariaApp'
        db_table = 'Usuario'
    
class Mascota(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    nombre = models.CharField(max_length=200)
    cedula_dueño = models.CharField(max_length=200)
    edad = models.CharField(max_length=200)
    especie = models.CharField(max_length=200)
    raza = models.CharField(max_length=200)
    caracteristicas = models.CharField(max_length=200)
    peso = models.CharField(max_length=3)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    class Meta:
        app_label = 'veterinariaApp'
        db_table = 'Mascota'
    
class OrdenMascotas(models.Model):  
    id = models.CharField(max_length=200, primary_key=True)
    idMascota = models.CharField(max_length=200)
    cedulaDueno = models.CharField(max_length=200)
    cedulaVeterinario = models.CharField(max_length=200)
    nombreMedicamento = models.CharField(max_length=200)
    fechaHistoria = models.DateField
    
    class Meta:
        app_label = 'veterinariaApp'
        db_table = 'Orden'
    
    
    
    