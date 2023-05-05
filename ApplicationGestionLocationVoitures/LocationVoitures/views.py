from django.shortcuts import render, redirect
from .models import Client, Voiture, Reservation
from .Forms import VoitureForm
import json


# Admin Dashboard views

def homeds(resquest):
    client = Client.objects.all().count()
    voitures = Voiture.objects.all().count()
    reservations = Reservation.objects.all().count()
    filename = 'Scraping data/car_rentals.json'
    with open(filename) as file:
        data = json.load(file)
        count = len(data)
    file.close()
    return render(resquest, 'adminDashboard/home.html',
                  {'client': client, 'voiture': voitures, 'reservation': reservations, 'scraping': count})


def client_list(request):
    cls = Client.objects.all()
    return render(request, 'adminDashboard/client.html', {'cls': cls})


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
    return render(request, 'adminDashboard/scraped.html', {'cars': car_data})
