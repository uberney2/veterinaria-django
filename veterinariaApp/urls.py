from django.urls import path
from . import views


urlpatterns={
    path('', views.iniciar, name="inicio"),
    path('register/', views.register ),
    path('singup/',views.singup),
    path('administrator/', views.administrator ),
    path('singup/logout/',views.logout),
    path('hc/', views.crearHistoriaClinica, name = 'hc' )

}