# Application de Location des voitures 
Notre application web est une plateforme de location de voitures développée avec Django. Elle permet aux utilisateurs de rechercher, louer et gérer leur location de voiture en ligne.

## Fonctionnalités
* Recherche de voitures disponibles.
* Réservation de voiture en ligne.
* Gestion des réservations pour les utilisateurs enregistrés.
* Système de paiement en ligne sécurisé pour le paiement des réservations avec **Paypal**.
* Tableau de bord administrateur pour la gestion des voitures et des réservations.
* Scraping des données : scraping des voitures depuis le site **[discovercars](https://www.discovercars.com/fr/morocco?keyword=location%20voiture%20maroc&network=g&gclid=CjwKCAjw586hBhBrEiwAQYEnHeFSL-3_5SYsg8X5poNJrK4MpY6DHH7XKuE2f8XJYQgQXfQ904ZvCRoCsCQQAvD_BwE)**
## Technologies utilisées

  - Django framework
  - HTML/CSS/JavaScript pour l'interface utilisateur et d'administrateur
  - MySQL pour la base de données
  - django-paypal pour le traitement des paiements en ligne
  
## Installation

1. Clonez le dépôt GitHub : git clone https://github.com/soulohabdellah/Application-location-voitures-django.git
2. Configurez votre environnement python 
3. Installez les dépendances requises : pip install -r requirements.txt 
4. Appliquez les migrations pour la base de données : python manage.py migrate
5. Lancez le serveur : python manage.py runserver

## Auteur

* [AIMAD EDDINE Yousri](https://github.com/yaimadeddine)
* [SOULOH Abdellah](https://github.com/soulohabdellah)
* [OUASSEN Rida](https://github.com/Ouassen123)
