from django.urls import path
from back import views


urlpatterns = [
    path('',views.home, name="Home"),
    path('perfil/',views.perfil, name="Perfil"),
    path('sitios/',views.sitios, name="Sitios"),
]
