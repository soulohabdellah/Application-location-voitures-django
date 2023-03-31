
from django.urls import path

from .views import voitures,voiture,GestionVoitures,contact,AjouterVoiture,Home,Reservation,AuthentificationClient,CreateCompte
urlpatterns = [
path('reserver',voitures, name='voitures'),
    path('',Home),
path('authentification-client',AuthentificationClient),
    path('reservation/', Reservation, name='voiture'),
    path('voiture/<int:voiture_id>/',voiture, name='voiture'),
    path('contact/',contact),
    path('gestion-cars/',GestionVoitures,name='voitures'),
    path('gestion-cars/add-car', AjouterVoiture),
    path('create-account/', CreateCompte, name='voiture'),

]
