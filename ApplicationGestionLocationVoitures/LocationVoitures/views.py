from django.shortcuts import render
from .models import Client, Voiture, Reservation


# Admin Dashboard views

def homeds(resquest):
    return render(resquest, 'adminDashboard/home.html')


def client_list(request):
    cls = Client.objects.all()
    return render(request, 'adminDashboard/client.html', {'cls': cls})


def voiture_list(request):
    voitures = Voiture.objects.all()
    return render(request, 'adminDashboard/voiture.html', {'voitures': voitures})


def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'adminDashboard/reservation.html', {'reservations': reservations})
