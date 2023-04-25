from django import forms
from .models import Client, Message, Voiture


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['Email', 'Nom', 'Message']


class ClientAuthentificationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['Email', 'Password']


class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = '__all__'
