from django.shortcuts import render,get_object_or_404,redirect
from .models import Voiture,Client,Reservation
from django.contrib.auth import logout
from .models import Voiture
from .Forms import ClientForm,MessageForm,ClientAuthentificationForm
from  django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from datetime import datetime
def voitures(request):
    voitures=Voiture.objects.all()
    return  render(request,'InterfaceClient/NosVehicules.html',{'voitures':voitures})
def voiture(request,voiture_id):
    voiture=get_object_or_404(Voiture,id=voiture_id)
    return  render(request,'InterfaceClient/voiture_detail.html',{'voiture':voiture})

def contact(request):
        client_id = request.session.get('client_id')
        if client_id:
            return render(request, 'InterfaceClient/Contact.html', {'message': ''})
        else:
            return render(request, 'InterfaceClient/AuthentificationClient.html', {'message': ''})


def GestionVoitures(request):
    voitures=Voiture.objects.all()
    return  render(request,'InterfaceClient/GestionVoitures.html',{'voitures':voitures})
def AjouterVoiture(request):
    return  render(request,'InterfaceClient/AjouterVoiture.html')
def Home(request):
    return render(request,'InterfaceClient/Home.html')
def ReservationVoiture(request,voiture_id):
    client_id = request.session.get('client_id')
    if 'voiture_id' in request.session:
     del request.session['voiture_id']
    request.session['voiture_id'] = voiture_id
    voiture = get_object_or_404(Voiture, id=voiture_id)
    if client_id:
        return render(request, 'InterfaceClient/InfoReservation.html', {'voiture': voiture})
    else:
        return  render(request,'InterfaceClient/AuthentificationClient.html')

def AuthentificationClient(request):

    return  render(request,'InterfaceClient/AuthentificationClient.html')
def CreateCompte(request):

    return  render(request,'InterfaceClient/InscriptionClient.html')
def AjouterClient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            client = form.save(commit=False)
            client.Password = make_password(form.cleaned_data['Password'])
            client.save()
            request.session['client_id'] = client.id
            request.session['client_name'] = client.Nom

            return redirect('/location-voitures')
    else:
        form = ClientForm()
    return render(request, 'InterfaceClient/Home.html', {'form': form})

def CreerMessage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'InterfaceClient/Contact.html', {'message': 'Message bien envoyée'})
    else:
        form = MessageForm()
    return render(request, 'InterfaceClient/Home.html', {'form': form})

def GestionAuthentification(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['Password']
        clients = Client.objects.filter(Email=email)
        if not clients:
            error_message = 'Invalid email or password'
            form = ClientAuthentificationForm()
            return render(request, 'InterfaceClient/AuthentificationClient.html', {'form': form, 'error_message': error_message})
        for client in clients:
            if check_password(password, client.Password):
                request.session['client_id'] = client.id
                request.session['client_name'] = client.Nom
                return redirect('/location-voitures')
        error_message = 'Invalid email or password'
        form = ClientAuthentificationForm()
        return render(request, 'InterfaceClient/AuthentificationClient.html', {'form': form, 'error_message': error_message})
    else:
        form = ClientAuthentificationForm()
    return render(request, 'InterfaceClient/AuthentificationClient.html', {'form': form})

def ReservationInfo(request):
    return render(request, 'InterfaceClient/InfoReservation.html')

def CreateReservation(request):

    format_string = "%d/%m/%Y %H:%M:%S"
    if request.method == 'POST':
        myvoiture_id = request.session.get('voiture_id')
        myclient_id = request.session.get('client_id')
        if not myvoiture_id or not myclient_id:
            return render(request, 'InterfaceClient/InfoReservation.html')
        myvoiture = get_object_or_404(Voiture, id=myvoiture_id)
        myclient = get_object_or_404(Client, id=myclient_id)
        date_debut = datetime.strptime(request.POST['debut'], format_string).date()
        date_fin = datetime.strptime(request.POST['arrive'], format_string).date()
        diff = (date_fin - date_debut).days
        prixtotal=diff*myvoiture.PrixDeLocation
        reservation = Reservation(client=myclient, voiture=myvoiture, date_debut=date_debut, date_fin=date_fin, prix_total=prixtotal)
        reservation.save()
        return render(request, 'InterfaceClient/Home.html')

def deconnexion(request):
    if 'client_id' in request.session:
        del request.session['client_id']
    if 'voiture_id' in request.session:
        del request.session['voiture_id']
    logout(request)
    return redirect('/location-voitures')
