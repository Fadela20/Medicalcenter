from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.liste_patients, name='liste_patients'),
    path('patients/ajouter/', views.ajouter_patient, name='ajouter_patient'),
]
  