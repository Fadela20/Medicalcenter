from django.db import models
from django.utils import timezone


class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    sexe = models.CharField(
        max_length=10,
        choices=[('Homme', 'Homme'), ('Femme', 'Femme')]
    )
    telephone = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    antecedents = models.TextField(blank=True, null=True)
    date_enregistrement=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_heure = models.DateTimeField()
    motif = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rendez-vous de {self.patient} le {self.date_heure.strftime('%Y-%m-%d %H:%M')}"

class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_heure = models.DateTimeField(default=timezone.now)
    diagnostic = models.TextField()
    traitement = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consultation de {self.patient} le {self.date_heure.strftime('%Y-%m-%d %H:%M')}"

class Ordonnance(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    medicaments = models.TextField()
    instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Ordonnance pour {self.consultation.patient} le {self.consultation.date_heure.strftime('%Y-%m-%d')}"
    
class DocumentMedical(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    type_document = models.CharField(max_length=50,
                                     choices=[
                                         ('radio', 'Radiographie'), ('Analyse ', 'Analyse '), ('irm', 'IRM'),('Autre', 'Autre')
                                         ],default='Autre'
    )
    fichier = models.FileField(upload_to='documents_medicals/')
    date_ajout = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Document: {self.titre} pour {self.patient}"
