from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.liste_patients, name='liste_patients'),
    path('patients/ajouter/', views.ajouter_patient, name='ajouter_patient'),
    path ('patients/modifier/<int:pk>/',views.modifier_patient,name='modifier_patient'),
    path('patients/supprimer/<int:pk>/',views.supprimer_patient,name='supprimer_patient'),
    path ('',views.dashboard,name='dashboard'),
]
  