from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.liste_patients, name='liste_patients'),
    path('patients/ajouter/', views.ajouter_patient, name='ajouter_patient'),
    path('patients/modifier/<int:pk>/', views.modifier_patient, name='modifier_patient'),
    path('patients/supprimer/<int:pk>/', views.supprimer_patient, name='supprimer_patient'),
    path('', views.dashboard, name='dashboard'),
    path('patients/<int:patient_id>/ajouter_document/', views.ajouter_document, name='ajouter_document'),
    path('document/<int:document_id>/supprimer/', views.supprimer_document, name='supprimer_document'),
    path('document/<int:document_id>/modifier/', views.modifier_document, name='modifier_document'),
    path('patients/<int:patient_id>/rendezvous/ajouter/', views.ajouter_rendez_vous, name='ajouter_rendez_vous'),
    path('documents/', views.liste_documents, name='liste_documents'),
    path('rendezvous/', views.liste_rendez_vous, name='liste_rendez_vous'),
    
    
    
]
  