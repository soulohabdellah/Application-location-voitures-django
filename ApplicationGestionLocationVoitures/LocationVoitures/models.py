from django.db import models

class Voiture(models.Model):
    Name = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Marque=models.CharField(max_length=100)
    Kilometrage=models.IntegerField(max_length=100,default=0)
    Couleur = models.CharField(max_length=100, default='Noir')
    NombrePlaces = models.IntegerField(max_length=100, default=5)
    BoiteVitesse = models.CharField(max_length=100, default='Automatique')
    PrixDeLocation = models.FloatField( default=300)
    MainImage = models.CharField(max_length=100,default='default.jpg')
class Client(models.Model):
    CinOrPassportId = models.CharField(max_length=25)
    Email = models.CharField(max_length=100)
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    Password = models.CharField(max_length=250)
    Telephone = models.CharField(max_length=30)
    Adresse = models.CharField(max_length=200)
class Message(models.Model):
    Email = models.CharField(max_length=100)
    Nom = models.CharField(max_length=20)
    Message = models.CharField(max_length=1000)
    Lu=models.BooleanField(default=False)

class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    prix_total = models.FloatField()
    def __init__(self, client=None, voiture=None, date_debut=None, date_fin=None, prix_total=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = client
        self.voiture = voiture
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.prix_total = prix_total


