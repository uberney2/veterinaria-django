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
    path('crear-historia/', views.desarrolloHistoriaClinica, name = 'crear-historia' ),
    path('editar-historia/', views.editarHistoriaClinica, name = 'editar-historia' ),
    path('listar-historia/<str:id>', views.listarHistoriaClinica, name = 'listar-historia' ),
    path('editar-historia-clinica/<str:id>', views.edicionHistoriaClinica, name = 'editar-historia-clinica' ),
    path('cancelar-orden/', views.cancelarOrden, name = 'cancelar-orden' ),
    path('confirmacion-cancelar-orden/<str:id>', views.confirmacionCancelacionOrden, name = 'confirmacion-cancelar-orden' )
]
