from django.shortcuts import render,get_object_or_404
from .models import Voiture
def voitures(request):
    voitures=Voiture.objects.all()
    return  render(request,'Home.html',{'voitures':voitures})
def voiture(request,voiture_id):
    voiture=get_object_or_404(Voiture,id=voiture_id)
    return  render(request,'voiture_detail.html',{'voiture':voiture})