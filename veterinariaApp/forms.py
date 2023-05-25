from django import forms

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
