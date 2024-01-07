from django import forms

from flashcardApp.models import FlashcardGroup


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label="Login")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label="Hasło")


class RegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label="Imię")
    mail = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label="E-mail")
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label="Login")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label="Hasło")