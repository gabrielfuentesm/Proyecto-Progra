from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('hlascondes', views.Lascondes, name="hlascondes"), 
    path('contacto', views.contacto, name="contacto"),
    path('hlareina', views.lareina, name="hlareina"),
    path('hprovidencia', views.providencia, name="hprovidencia"),
    path('hvitacura', views.vitacura, name="hvitacura"),
    path('respuesta', views.respuesta, name="respuesta"),
    path('hbarnechea', views.lobarnechea, name="hbarnechea"),
    path('inicio2', views.inicio2, name="inicio2"),
    path('ubiclascondes', views.ubic_lascondes, name="ubiclascondes"),
    path('ubicvitacura', views.ubic_vitacura, name="ubicvitacura"),
    path('ubiclobarnechea', views.ubic_lobarnechea, name="ubiclobarnechea"),
    path('ubicprovi', views.ubic_provi, name="ubicprovi"),
    path('ubiclareina', views.ubic_lareina, name="ubiclareina"),  
]