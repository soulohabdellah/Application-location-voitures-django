from django.shortcuts import render,get_object_or_404,redirect
from .models import Voiture,Client
from .Forms import ClientForm,MessageForm,ClientAuthentificationForm
from  django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

def voitures(request):
    voitures=Voiture.objects.all()
    return  render(request,'NosVehicules.html',{'voitures':voitures})
def voiture(request,voiture_id):
    voiture=get_object_or_404(Voiture,id=voiture_id)
    return  render(request,'voiture_detail.html',{'voiture':voiture})
@login_required(login_url='/location-voitures/authentification-client')
def contact(request):
    return render(request, 'Contact.html',{'message':' '})
def GestionVoitures(request):
    voitures=Voiture.objects.all()
    return  render(request,'GestionVoitures.html',{'voitures':voitures})
def AjouterVoiture(request):
    return  render(request,'AjouterVoiture.html')
def Home(request):
    return render(request,'Home.html')
def Reservation(request):

    return  render(request,'AuthentificationClient.html')
def AuthentificationClient(request):

    return  render(request,'AuthentificationClient.html')
def CreateCompte(request):

    return  render(request,'InscriptionClient.html')
def AjouterClient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.Password = make_password(form.cleaned_data['Password'])
            client.save()
            return redirect('/location-voitures')
    else:
        form = ClientForm()
    return render(request, 'Home.html', {'form': form})

def CreerMessage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Contact.html', {'message': 'Message bien envoyée'})
    else:
        form = MessageForm()
    return render(request, 'Home.html', {'form': form})
def GestionAuthentification(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['Password']
        clients = Client.objects.filter(Email=email)
        if not clients:
            error_message = 'Invalid email or password'
            form = ClientAuthentificationForm()
            return render(request, 'AuthentificationClient.html', {'form': form, 'error_message': error_message})
        for client in clients:
            if check_password(password, client.Password):
                return redirect('/location-voitures')
        error_message = 'Invalid email or password'
        form = ClientAuthentificationForm()
        return render(request, 'AuthentificationClient.html', {'form': form, 'error_message': error_message})
    else:
        form = ClientAuthentificationForm()
    return render(request, 'AuthentificationClient.html', {'form': form})