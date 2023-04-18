from django.db import models


class Voiture(models.Model):
    Name = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Marque = models.CharField(max_length=100)
    Kilometrage = models.IntegerField(default=0)
    Couleur = models.CharField(max_length=100, default='Noir')
    NombrePlaces = models.IntegerField(default=5)
    Climat = models.BooleanField(default=True)
    BoiteVitesse = models.CharField(max_length=100, default='Automatique')
    PrixDeLocation = models.FloatField(default=300)
    Disponible = models.BooleanField(default=True)
    MainImage = models.CharField(max_length=100, default='default.jpg')
    Description = models.CharField(max_length=1000, default=' ')


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
    Lu = models.BooleanField(default=False)


class Reservation(models.Model):
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    prix_total = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)

    def __init__(self, client, voiture, date_debut, date_fin, prix_total, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = client
        self.voiture = voiture
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.prix_total = prix_total

    @classmethod
    def FindByClient(cls, client_id):
        reservations = cls.objects.filter(client_id=client_id).values_list('prix_total', 'date_debut', 'date_fin',
                                                                           'voiture__Name')
        listres = [{'prix': item[0], 'debut': item[1].strftime('%d/%m/%Y'), 'fin': item[2].strftime('%d/%m/%Y'),
                    'voiture': item[3]} for item in reservations]
        return listres
