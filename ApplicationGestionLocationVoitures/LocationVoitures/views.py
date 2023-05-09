from django.shortcuts import render, redirect
from .models import Client, Voiture, Reservation, Message
from .Forms import VoitureForm, ClientForm ,MessageForm
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .Forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Admin Dashboard views

def homeds(resquest):
    client = Client.objects.all().count()
    voitures = Voiture.objects.all().count()
    reservations = Reservation.objects.all().count()
    messages = Message.objects.all().count()
    filename = 'Scraping data/car_rentals.json'
    with open(filename) as file:
        data = json.load(file)
        count = len(data)
    file.close()
    return render(resquest, 'adminDashboard/home.html',
                  {'client': client, 'voiture': voitures, 'reservation': reservations, 'scraping': count, 'message': messages})


def client_list(request):
    cls = Client.objects.all()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-url')
    else:
        form = ClientForm()
    return render(request, 'adminDashboard/client.html', {'cls': cls,'form': form})


def voiture_list(request):
    voitures = Voiture.objects.all()
    if request.method == 'POST':
        form = VoitureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voiture-url')
    else:
        form = VoitureForm()
    return render(request, 'adminDashboard/voiture.html', {'voitures': voitures, 'form': form})


def reservation_list(request):
    reservations = Reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'adminDashboard/reservation.html', context)

def message_list(request):
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, 'adminDashboard/message.html', context)



# def create_car(request):
#     if request.method == 'POST':
#         form = VoitureForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('voiture_list')
#         else:
#             form = VoitureForm()
#         return render(request, 'adminDashboard/reservation.html', {'form': form})

def scraped_list(request):
    with open('Scraping data/car_rentals.json', 'r') as f:
        car_data = json.load(f)
    if request.method == 'POST':
        form = VoitureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voiture-url')
    else:
        form = VoitureForm()
    return render(request, 'adminDashboard/scraped.html', {'cars': car_data, 'form': form})


# login_admin
from django.shortcuts import redirect

from django.shortcuts import redirect


def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                if username == 'admin' and password == 'admin':
                    return redirect('http://localhost:8000/location-voitures/admin')
                else:
                    login(request, user)
                    return redirect('home')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = AuthenticationForm()
    return render(request, 'adminDashboard/login.html', {'form': form})
