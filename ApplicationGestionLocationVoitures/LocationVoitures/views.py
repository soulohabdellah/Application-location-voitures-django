from django.shortcuts import render,get_object_or_404
from .models import Voiture
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
def Reservation(request,voiture_id):
    voiture=get_object_or_404(Voiture,id=voiture_id)
    return  render(request,'AuthentificationClient.html',{'voiture':voiture})
def AuthentificationClient(request):

    return  render(request,'AuthentificationClient.html')