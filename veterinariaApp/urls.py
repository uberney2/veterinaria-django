from django.urls import path
from . import views


urlpatterns=[
    path('', views.iniciar, name="inicio"),
    path('', views.index),
    path('medicina/', views.medicina),
    path('register/', views.register ),
    path('singup/',views.singup),
    path('administrator/', views.administrator ),
    path('singup/logout/',views.logout),
    path('hc/', views.crearHistoriaClinica, name = 'hc' ),
    path('dueño-mascota/', views.crearDueñoMascota, name = 'dueño' ),
    path('mascota/', views.crearMascota, name = 'mascota' ),
    path('vendedor/', views.vendedor),
    path('ventaSinOrden/', views.ventaSinOrden, name="venta_sin_orden"),
    path('ventaConOrden/', views.ventaConOrden, name="venta_con_orden"),
]
