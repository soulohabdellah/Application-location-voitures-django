
from django.urls import path

from .views import voitures,voiture,GestionVoitures,contact,AjouterVoiture,Home,Reservation,AuthentificationClient,CreateCompte,AjouterClient,CreerMessage,GestionAuthentification,ReservationInfo,deconnexion
urlpatterns = [
path('reserver',voitures, name='voitures'),
    path('',Home),
path('authentification-client',AuthentificationClient),
path('deconnexion/', deconnexion, name='voiture'),
    path('reservation/<int:voiture_id>/', Reservation, name='voiture'),
    path('reservation/info', ReservationInfo, name='voiture'),
    path('voiture/<int:voiture_id>/',voiture, name='voiture'),
    path('contact/',contact),
    path('contact/message', CreerMessage),
    path('gestion-cars/',GestionVoitures,name='voitures'),
    path('gestion-cars/add-car', AjouterVoiture),
    path('create-account/', CreateCompte, name='voiture'),
    path('create-account/add-user', AjouterClient, name='voiture'),
    path('authentification-client/authentifier',GestionAuthentification),

]
