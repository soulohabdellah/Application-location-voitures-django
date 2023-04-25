from django.shortcuts import render, redirect
from .models import Client, Voiture, Reservation
from .Forms import VoitureForm


# Admin Dashboard views

def homeds(resquest):
    return render(resquest, 'adminDashboard/home.html')


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


def create_car(request):
    if request.method == 'POST':
        form = VoitureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voiture_list')
        else:
            form = VoitureForm()
        return render(request, 'adminDashboard/reservation.html', {'form': form})
