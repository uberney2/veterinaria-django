from django import forms

from veterinariaApp.Enums.rolesEnum import Roles

class CrearFormHistoriaClinica(forms.Form):
    motivoConsulta = forms.CharField(label="Motivo consulta", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    medicamento = forms.CharField(label="Medicamento", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    dosis = forms.CharField(label="Dosis", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    sintomatologia =  forms.CharField(label="Sintomatologia", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    diagnostico = forms.CharField(label="Diagnostico", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    procedimiento = forms.CharField(label="Procedimiento", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    historialVacunacion = forms.CharField(label="Historial de vacunacion", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    alergiasMedicamentos = forms.CharField(label="Alergias a medicamentos", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    detalleProcedimiento = forms.CharField(label="Detalles del Procedimiento", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    
class AgregarDueñoMascotaForm(forms.Form):
    cedula = forms.CharField(label="Cedula", max_length=20, widget=forms.TextInput(attrs={'class': 'input'}))
    nombre = forms.CharField(label="Nombre Completo", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    edad = forms.CharField(label="Edad", max_length=3, widget=forms.TextInput(attrs={'class': 'input'}))
    
class AgregarMascotaForm(forms.Form):
    nombre = forms.CharField(label="Nombre mascota", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    cedula_dueño = forms.CharField(label="Cedula del dueño", max_length=20, widget=forms.TextInput(attrs={'class': 'input'}))
    edad = forms.CharField(label="Edad", max_length=3, widget=forms.TextInput(attrs={'class': 'input'}))
    especie = forms.CharField(label="Especie", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    raza = forms.CharField(label="Raza", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    caracteristicas = forms.CharField(label="Caracteristicas", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    peso = forms.CharField(label="Peso", max_length=3, widget=forms.TextInput(attrs={'class': 'input'}))

class ventaSinOrden(forms.Form):
    cedula_comprador = forms.CharField(label="Ingrese su cedula", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    medicamento = forms.CharField(label="Ingrese el medicamento", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    cantidad = forms.CharField(label="Ingrese la cantidad", max_length=3, widget=forms.TextInput(attrs={'class': 'input'}))
    valor_venta = forms.CharField(label="Ingrese la cantidad", max_length=3, widget=forms.TextInput(attrs={'class': 'input'}))
    
class BuscarUsuarioForm(forms.Form):
    cedula_dueño = forms.CharField(label="Cedula del dueño de la mascota", max_length=20, widget=forms.TextInput(attrs={'class': 'input'}))
    
class comenzarCreaciónHistoriaClinicaForm(forms.Form):
    idMascota = forms.CharField(label="Identificación de la mascota", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))

