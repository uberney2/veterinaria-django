from django.urls import path,include
from . import views
import debug_toolbar;


urlpatterns=[
     path('__debug__/', include(debug_toolbar.urls)),
    path('', views.iniciar, name='inicio'),
    path('register/', views.register, name='register'),
    path('singup/',views.singup, name='singup'),
    path('administrator/', views.administrator, name='admin' ),
    path('singup/logout/',views.logout,name='logout'),
    path('hc/', views.crearHistoriaClinica, name = 'hc' ),
    path('dueño-mascota/', views.crearDueñoMascota, name = 'dueño' ),
    path('mascota/', views.crearMascota, name = 'mascota' ),
    path('error/<str:user_id>/delete', views.eliminarUser, name = 'delete' ),
]