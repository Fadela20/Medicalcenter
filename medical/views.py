from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Patient,DocumentMedical,RendezVous
from .forms import PatientForm,DocumentMedicalForm,RendezVousForm   
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
    total_documents=DocumentMedical.objects.count()
    total_rendez_vous=RendezVous.objects.count()
    derniers_patients=Patient.objects.order_by('-date_enregistrement')[:5]
    
    
    context ={
        'total_patients':total_patients,
        'total_documents':total_documents,
        'total_rendez_vous':total_rendez_vous,
        'derniers_patients':derniers_patients
    }
    return render(request,'dashboard.html',context)

def ajouter_document(request , patient_id):
    patient =get_object_or_404(Patient,id=patient_id)
    if request.method == 'POST':
        form = DocumentMedicalForm(request.POST,request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.patient = patient
            document.save()
            return redirect('liste_patients')
    else:
        form = DocumentMedicalForm()
    return render(request, 'ajouter_document.html', {'form': form, 'patient': patient})
        
def detail_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    documents = patient.documentmedical_set.all().order_by('-date_ajout')
    rendez_vous_list = patient.rendezvous_set.all().order_by('date_heure')
    return render(request, 'detail_patient.html', {'patient': patient, 'documents': documents, 'rendez_vous_list': rendez_vous_list})

def supprimer_document(request,document_id):
    document =get_object_or_404(DocumentMedical, id=document_id)
    patient_id=document.patient.id
    document.delete()
    messages.success(request,"Le document a été supprimé avec succès")
    return redirect('detail_patient',patient_id=patient_id)

def modifier_document(request,document_id):
    document=get_object_or_404(DocumentMedical,id=document_id)
    if request.method == 'POST':
        form =DocumentMedicalForm(request.POST , request.FILES,instance=document)
        if form.is_valid():
            form.save()
            messages.success(request,"Le document a été modifié avec succés.")
            return redirect('detail_patient',patient_id=document.patient.id)
        else:
            form=DocumentMedicalForm(instance=document)
        return render(request,'medical/modifier_document.html',{'form':form,'document':document})
    
def ajouter_rendez_vous(request,patient_id):
    patient=get_object_or_404(Patient,id=patient_id)
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            rendez_vous = form.save(commit=False)
            rendez_vous.patient = patient
            rendez_vous.save()
            messages.success(request,"Le rendez-vous a été ajouté avec succès.")
            return redirect('detail_patient',patient_id=patient.id)
        else:
            form = RendezVousForm()
    return render(request,'medical/ajouter_rendez_vous.html',{'form': form, 'patient':patient})

def liste_rendez_vous(request,patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    rendez_vous_list=RendezVous.objects.all().order_by('date_heure')
    return render(request, 'medical/liste_rendez_vous.html', {'patient': None, 'rendez_vous_list': rendez_vous_list}) 


def liste_documents(request):
    documents = DocumentMedical.objects.all()
    return render(request, 'medical/liste_documents.html', {'documents': documents})  
    
    
        