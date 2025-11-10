from django.db import models

from django.db import models

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
    date_enregistrement=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

