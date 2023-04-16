from django.shortcuts import render, get_object_or_404, redirect
from .models import Voiture, Client, Reservation,Message
from django.contrib.auth import logout
from .models import Voiture
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from datetime import datetime


def voitures(request):
    voitures = Voiture.objects.filter(Disponible=True)
    return render(request, 'InterfaceClient/NosVehicules.html', {'voitures': voitures})


def voiture(request, voiture_id):
    voiture = get_object_or_404(Voiture, id=voiture_id, Disponible=True)
    if voiture:
        return render(request, 'InterfaceClient/voiture_detail.html', {'voiture': voiture})
    else:
        return render(request, 'InterfaceClient/NosVehicules.html',
                      {'voitures': voitures, 'message': 'Voiture introuvable'})


def contact(request):
    return render(request, 'InterfaceClient/Contact.html')


def Home(request):
    return render(request, 'InterfaceClient/Home.html')


def ReservationVoiture(request, voiture_id):
    client_id = request.session.get('client_id')
    if client_id:
        if 'voiture_id' in request.session:
            del request.session['voiture_id']
        request.session['voiture_id'] = voiture_id
        voiture = get_object_or_404(Voiture, id=voiture_id)
        return render(request, 'InterfaceClient/InfoReservation.html', {'voiture': voiture})
    else:
        return render(request, 'InterfaceClient/AuthentificationClient.html')


def AuthentificationClient(request):
    return render(request, 'InterfaceClient/AuthentificationClient.html')


def CreateCompte(request):
    return render(request, 'InterfaceClient/InscriptionClient.html')


def AjouterClient(request):
    if request.method == 'POST':
        email = request.POST['email']
        cin_or_passport_id = request.POST['CinOrPassportId']
        prenom = request.POST['Prenom']
        nom = request.POST['Nom']
        telephone = request.POST['Telephone']
        adresse = request.POST['Adresse']
        password = make_password(request.POST['Password'])
        if Client.objects.filter(Email=email).exists():
                return render(request, 'InterfaceClient/InscriptionClient.html', {'message': 'Email exist'})
        else:
                client = Client(Nom=nom,Prenom=prenom,Email=email,Password=password, CinOrPassportId=cin_or_passport_id, Telephone=telephone,Adresse=adresse)
                client.save()
                request.session['client_id'] = client.id
                request.session['client_name'] = client.Nom
                return redirect('/location-voitures')



def CreerMessage(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        nouveau_message = Message(Nom=nom, Email=email, Message=message)
        nouveau_message.save()
        return render(request, 'InterfaceClient/Contact.html', {'message': 'Message bien envoyé'})
    else:
        return render(request, 'InterfaceClient/Home.html')
def GestionAuthentification(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['Password']
        clients = Client.objects.filter(Email=email)
        if not clients:
            error_message = 'Mot de passe ou email pas correct'
            form = ClientAuthentificationForm()
            return render(request, 'InterfaceClient/AuthentificationClient.html',
                          {'form': form, 'message': error_message})
        for client in clients:
            if check_password(password, client.Password):
                request.session['client_id'] = client.id
                request.session['client_name'] = client.Nom
                return redirect('/location-voitures')
        error_message = 'Mot de passe ou email pas correct'
        form = ClientAuthentificationForm()
        return render(request, 'InterfaceClient/AuthentificationClient.html', {'form': form, 'message': error_message})
    else:
        form = ClientAuthentificationForm()
    return render(request, 'InterfaceClient/AuthentificationClient.html', {'form': form})


def ReservationInfo(request):
    client_id = request.session.get('client_id')
    if client_id:
        return render(request, 'InterfaceClient/InfoReservation.html')
    else:
        return render(request, 'InterfaceClient/AuthentificationClient.html')


def CreateReservation(request):
    client_id = request.session.get('client_id')
    if client_id:
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
            prixtotal = diff * myvoiture.PrixDeLocation
            reservation = Reservation(client=myclient, voiture=myvoiture, date_debut=date_debut, date_fin=date_fin,
                                      prix_total=prixtotal)
            reservation.save()
            myvoiture.Disponible = False
            myvoiture.save()
            if 'voiture_id' in request.session:
                del request.session['voiture_id']
                client_id = request.session.get('client_id')
                if client_id:
                    reservations = Reservation.FindByClient(client_id)
                    myclient = get_object_or_404(Client, id=client_id)
                    return render(request, 'InterfaceClient/ProfilClient.html',{'reservations': reservations, 'client': myclient,'message': 'Reservation bien creer'})
    else:
        return render(request, 'InterfaceClient/AuthentificationClient.html')


def ProfilClient(request):
    client_id = request.session.get('client_id')
    if client_id:
        reservations = Reservation.FindByClient(client_id)
        myclient = get_object_or_404(Client, id=client_id)
        return render(request, 'InterfaceClient/ProfilClient.html', {'reservations': reservations, 'client': myclient})
    else:
        return render(request, 'InterfaceClient/AuthentificationClient.html')


def deconnexion(request):
    if 'client_id' in request.session:
        del request.session['client_id']
    if 'voiture_id' in request.session:
        del request.session['voiture_id']
    logout(request)
    return redirect('/location-voitures')


def UpdateCompte(request):
    client_id = request.session.get('client_id')

    if client_id:
        if request.method == 'POST':
            client = get_object_or_404(Client, id=client_id)
            client.CinOrPassportId = request.POST.get('CinOrPassportId')
            client.Email = request.POST.get('Email')
            client.Nom = request.POST.get('Nom')
            client.Prenom = request.POST.get('Prenom')
            client.Telephone = request.POST.get('Telephone')
            client.Adresse = request.POST.get('Adresse')
            client.Password = make_password(request.POST.get('Password'))
            client.save()
            return redirect('/location-voitures/profil/')
    else:
        return render(request, 'InterfaceClient/AuthentificationClient.html')


def search(request, voiture_name):
    try:
        voiture = Voiture.objects.get(Name=voiture_name,Disponible=True)
    except Voiture.DoesNotExist:
        voiture = None
    if voiture:
        return render(request, 'InterfaceClient/voiture_detail.html', {'voiture': voiture})
    else:
        return render(request, 'InterfaceClient/Home.html',{'message': 'Voiture introuvable'})
