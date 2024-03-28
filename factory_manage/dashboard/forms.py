from django import forms

class AdminRegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)

class FarmerRegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
