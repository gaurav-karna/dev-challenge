from django.shortcuts import render, redirect

#from .models import

#from .forms import EmailForm

# Email imports
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string

# Create your views here.

def index (request):
    return render(request, 'base.html', {})

def success (request):
    return render (request, 'base.html', {})
