
from django.urls import path

from .viewClient import voitures,voiture,contact,Home,ProfilClient,ReservationVoiture,AuthentificationClient,CreateCompte,AjouterClient,CreerMessage,GestionAuthentification,ReservationInfo,deconnexion,CreateReservation
urlpatterns = [
    path('reserver',voitures, name='voitures'),
    path('',Home),
    path('authentification-client',AuthentificationClient),
    path('deconnexion/', deconnexion, name='voiture'),
    path('reservation/<int:voiture_id>/', ReservationVoiture, name='voiture'),
    path('reservation/info', ReservationInfo, name='voiture'),
    path('reservation/create-reservation', CreateReservation, name='voiture'),
    path('voiture/<int:voiture_id>/',voiture, name='voiture'),
    path('contact/',contact),
    path('contact/message', CreerMessage),
    path('profil/', ProfilClient),
    path('create-account/', CreateCompte, name='voiture'),
    path('create-account/add-user', AjouterClient, name='voiture'),
    path('authentification-client/authentifier',GestionAuthentification),

]
