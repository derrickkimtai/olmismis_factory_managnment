from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from farmers.models import Farmer


class AdminRegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)

class FarmerRegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'phone', 'address', 'id_number', 'berry_weight']

class FarmerWeightForm(forms.Form):
    Farmer = forms.CharField(label="Farmer's name", max_length=100)
    berry_weight = forms.FloatField(label="Coffe berries weight (kg)")