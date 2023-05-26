from django.urls import path
from . import views


urlpatterns=[
    path('', views.iniciar, name="inicio"),
    path('register/', views.register ),
    path('singup/',views.singup),
    path('administrator/', views.administrator ),
    path('singup/logout/',views.logout),
    path('hc/<str:id>', views.crearHistoriaClinica, name = 'hc' ),
    path('dueño-mascota/', views.crearDueñoMascota, name = 'dueño' ),
    path('mascota/', views.crearMascota, name = 'mascota' ),
    path('index-vet/', views.indexHistoriaClinica, name = 'veterinario' ),
    path('historia/', views.desarrolloHistoriaClinica, name = 'crear-historia' )

]