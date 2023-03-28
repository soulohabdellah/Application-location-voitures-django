
from django.urls import path

from .views import voitures,voiture
urlpatterns = [
    path('',voitures, name='voitures'),
    path('Voiture/<int:voiture_id>/',voiture, name='voiture'),
]
