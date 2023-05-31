from django.urls import path
from . import views


urlpatterns=[
    path('', views.iniciar, name='inicio'),
    path('register/', views.register, name='register'),
    path('singup/',views.singup, name='singup'),
    path('administrator/', views.administrator, name='admin' ),
    path('singup/logout/',views.logout,name='logout'),
    path('hc/<str:id>', views.crearHistoriaClinica, name = 'hc' ),
    path('dueño-mascota/', views.crearDueñoMascota, name = 'dueño' ),
    path('mascota/', views.crearMascota, name = 'mascota' ),
    path('index-vet/', views.indexHistoriaClinica, name = 'veterinario' ),
    path('crear-historia/', views.desarrolloHistoriaClinica, name = 'crear-historia' ),
    path('editar-historia/', views.editarHistoriaClinica, name = 'editar-historia' ),
    path('listar-historia/<str:id>', views.listarHistoriaClinica, name = 'listar-historia' ),
    path('editar-historia-clinica/<str:id>', views.edicionHistoriaClinica, name = 'editar-historia-clinica' ),
    path('cancelar-orden/', views.cancelarOrden, name = 'cancelar-orden' ),
    path('confirmacion-cancelar-orden/<str:id>', views.confirmacionCancelacionOrden, name = 'confirmacion-cancelar-orden' ),
    path('vendedor/', views.vendedor, name='vendedor'),
    path('ventaSinOrden/', views.ventaSinOrden, name='ventaSinOrden'),
    path('ventaConOrden/', views.ventaConOrden, name='ventaConOrden'),
    path('error/<str:user_id>/delete', views.eliminarUser, name = 'delete' ),
    path('comienzo-factura/', views.comienzoBuscarFacturas, name = 'factura' ),
    path('listar-facturas/<str:id>', views.listarFacturas, name = 'listar-factura' ),
]
