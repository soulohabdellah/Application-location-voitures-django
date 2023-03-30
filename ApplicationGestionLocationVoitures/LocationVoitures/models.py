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

