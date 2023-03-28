from django.db import models

class Voiture(models.Model):
    Name = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Marque=models.CharField(max_length=100)
    MainImage = models.CharField(max_length=100,default='default.jpg')
    pub_date=models.DateTimeField(auto_now_add=True)
