
from django.urls import path

from .views import voitures,voiture,GestionVoitures,contact,AjouterVoiture,Home,Reservation
urlpatterns = [
path('reserver',voitures, name='voitures'),
    path('',Home),
    path('reservation/<int:voiture_id>/', Reservation, name='voiture'),
    path('voiture/<int:voiture_id>/',voiture, name='voiture'),
    path('contact/',contact),
    path('gestion-cars/',GestionVoitures,name='voitures'),
    path('gestion-cars/add-car', AjouterVoiture),
]
