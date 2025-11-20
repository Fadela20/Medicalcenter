from django import forms
from .models import Patient,DocumentMedical,RendezVous

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom','prenom','date_naissance','telephone','adresse']
        
class DocumentMedicalForm(forms.ModelForm):
    class Meta:
        model =DocumentMedical
        fields =['titre','type_document','fichier']
        
class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['date_heure', 'motif', 'notes']
        widgets = {
            'date_heure': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
