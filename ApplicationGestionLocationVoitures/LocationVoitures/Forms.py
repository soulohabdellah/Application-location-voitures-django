from django import forms
from .models import Client, Message, Voiture
from django.contrib.auth.forms import AuthenticationForm


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



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
