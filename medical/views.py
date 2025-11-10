from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Patient
from .forms import PatientForm
from django.contrib.auth.decorators import login_required

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

def modifier_patient(request,pk):
    patient=get_object_or_404(Patient,pk=pk)
    if request.method =='POST':
        form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('liste_patients')
    else:
            form = PatientForm(instance=patient)
    return render(request,'patients/modifier.html',{'form':form,'patient':patient})
    
def supprimer_patient(request,pk):
    patient=get_object_or_404(Patient,pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('liste_patients')
    return render(request,'patients/supprimer.html',{'patient':patient})

@login_required
def dashboard(request):
    total_patients=Patient.objects.count()
    derniers_patients=Patient.objects.order_by('-date_enregistrement')[:5]
    
    context ={
        'total_patients':total_patients,
        'derniers_patients':derniers_patients
    }
    return render(request,'dashboard.html',context)
    
    
    
        