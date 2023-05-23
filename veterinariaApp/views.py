from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'shared/index.html')

def medicina(request):
    return render(request, 'medicamento/medicina.html')