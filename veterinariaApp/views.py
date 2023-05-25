import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from veterinariaApp.forms import CrearFormHistoriaClinica
from veterinariaApp.models import HistoriaClinica
from .conexionMongoDB import collection

# Create your views here.
def index(request):
    return render(request, 'shared/index.html')

def crearHistoriaClinica(request):
    if request.method == 'GET':
        return render(request, 'historia-clinica/historia_clinica.html',{
            'form': CrearFormHistoriaClinica()
        })
    else:
        hcJson = {}
        hcJson['_id'] = request.POST.get('_id', '')  # Acceder al campo _id usando request.POST.get()
        hcJson[request.POST.get('_id', '')] = {}  # Acceder al campo _id usando request.POST.get()
        hcJson[request.POST.get('_id', '')][request.POST['fechaConsulta']] = {
            "medicoVeterinario": request.POST['medicoVeterinario'],
            "motivoConsulta": request.POST['motivoConsulta'],
            "sintomatologia": request.POST['sintomatologia'],
            "diagnostico": request.POST['diagnostico'],
            "procedimiento": request.POST['procedimiento'],
            "medicamento": request.POST['medicamento'],
            "dosis": request.POST['dosis'],
            "idOrden": request.POST['idOrden'],
            "historialVacunacion": request.POST['historialVacunacion'],
            "alergiasMedicamentos": request.POST['alergiasMedicamentos'],
            "detalleProcedimiento": request.POST['detalleProcedimiento'],
            "estadoOrden": request.POST['estadoOrden']
        }
        print(hcJson)
        # hcJson.pop('_id', None)
        collection.insert_one(hcJson)
        # HistoriaClinica.objects.using('default').create(idMascota = hcJson['idMascota'], 
        #                                                 fechaConsulta=hcJson['fechaConsulta'],
        #                                                 medicoVeterinario=hcJson['medicoVeterinario'],
        #                                                 motivoConsulta=hcJson['motivoConsulta'],
        #                                                 sintomatologia=hcJson['sintomatologia'],
        #                                                 diagnostico=hcJson['diagnostico'],
        #                                                 procedimiento=hcJson['procedimiento'],
        #                                                 medicamento=hcJson['medicamento'],
        #                                                 dosis=hcJson['dosis'],
        #                                                 idOrden=hcJson['idOrden'],
        #                                                 historialVacunacion=hcJson['historialVacunacion'],
        #                                                 alergiasMedicamentos=hcJson['alergiasMedicamentos'],
        #                                                 detalleProcedimiento=hcJson['detalleProcedimiento'],
        #                                                 estadoOrden=hcJson['estadoOrden'])
        
        # HistoriaClinica.objects.using('default').create(hcJson)
        return redirect('hc')