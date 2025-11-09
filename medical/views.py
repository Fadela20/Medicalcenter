from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Patient
from .forms import PatientForm

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def liste_patients(request):
    patients = Patient.objects.all()
    return render(request, "patient_listes.html", {"patients": patients})

def ajouter_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_patients')
    else:
        form = PatientForm()
    return render(request, "ajouter.html", {"form": form})
