from django.shortcuts import render
from .forms import AdminRegistrationForm, FarmerRegistrationForm

# Create your views here.

def dashboard(request):
    if request.method == 'POST':
        if 'admin_form' in request.POST:
            form = AdminRegistrationForm(request.POST)
        elif 'farmer_form' in request.POST:
            form = FarmerRegistrationForm(request.POST)

    else:
        admin_form = AdminRegistrationForm()
        farmer_form = FarmerRegistrationForm()
        return render(request, 'registration/dashboard.html', {'admin_form': admin_form, 'farmer_form': farmer_form})