from django import forms

from veterinariaApp.Enums.rolesEnum import Roles

class CrearFormHistoriaClinica(forms.Form):
    _id = forms.CharField(label="Identificacion de la mascosta", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    fechaConsulta = forms.CharField(label="Fecha", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    medicoVeterinario = forms.CharField(label="Nombre del medico", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    motivoConsulta = forms.CharField(label="Motivo consulta", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    medicamento = forms.CharField(label="Medicamento", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    dosis = forms.CharField(label="Dosis", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    sintomatologia =  forms.CharField(label="Sintomatologia", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    diagnostico = forms.CharField(label="Diagnostico", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    procedimiento = forms.CharField(label="Procedimiento", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    idOrden = forms.CharField(label="Numero de orden", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    historialVacunacion = forms.CharField(label="Historial de vacunacion", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    alergiasMedicamentos = forms.CharField(label="Alergias a medicamentos", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    detalleProcedimiento = forms.CharField(label="Detalles del Procedimiento", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    estadoOrden = forms.CharField(label="Estado de la Orden", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    
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

class VentaSinOrden(forms.Form):
    #id = forms.CharField(label="Id producto", max_length=200,widget=forms.CharField(attrs={'class': 'input'}))
    producto =  forms.CharField(label="Producto",widget=forms.CharField(attrs={'class': 'input'}))
    valor = forms.DecimalField(label="Valor venta", widget=forms.DecimalField)  

class VentaConOrden(forms.Form):
    #id = forms.CharField(label="Id producto", max_length=200,widget=forms.CharField(attrs={'class': 'input'}))
    producto =  forms.CharField(label="Producto",widget=forms.CharField(attrs={'class': 'input'}))
    valor = forms.DecimalField(label="Valor venta", widget=forms.DecimalField) 