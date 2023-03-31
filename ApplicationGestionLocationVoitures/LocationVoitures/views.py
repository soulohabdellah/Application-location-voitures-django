from django.shortcuts import render,get_object_or_404,redirect
from .models import Voiture
from .Forms import ClientForm
def voitures(request):
    voitures=Voiture.objects.all()
    return  render(request,'NosVehicules.html',{'voitures':voitures})
def voiture(request,voiture_id):
    voiture=get_object_or_404(Voiture,id=voiture_id)
    return  render(request,'voiture_detail.html',{'voiture':voiture})
def contact(request):
    return render(request, 'Contact.html')
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
            form.save()
            return redirect('/location-voitures')
    else:
        form = ClientForm()
    return render(request, 'Home.html', {'form': form})
