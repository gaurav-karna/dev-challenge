from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Person, HackAdmin, User

from .forms import HackAdminForm, UserForm, PersonForm

# Email imports
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string

# Create your views here.

def index (request):
    return render (request, "base.html", {})

def success (request):
    if request.method == 'POST':
        person = PersonForm(request.POST)
        if person.is_valid():
            new_person = person.save()
            # triggers generic success page
            return render (request, 'success.html', {})
        else:
            context = {
                'error_message':'Invalid form submission, please check the email provided!'
            }
            return render (request, 'base.html', context)
    else:
        context = {
            'person_form':PersonForm(),
        }
        return render (request, 'base.html', {})

@login_required
@staff_member_required
def admin_home (request):
    # view will show all registered admins and users on different tabs
    admins = HackAdmin.objects.order_by('user.first_name')
    persons = Person.objects.order_by('First_name')
    context = {
        'user':request.user,
        'admins':admins,
        'persons':persons,
    }
    return render (request, 'admin_home.html', context)

@login_required
@staff_member_required
def create_admin (request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        admin_form = HackAdminForm(request.POST)
        if admin_form.is_valid() and user_form.is_valid():
            new_admin = user_form.save()
            new_admin_profile = admin_form.save(commit=False)
            new_admin.admin_profile = new_admin_profile
            new_admin_profile.user = new_admin
            new_admin.save()
            new_admin_profile.save()
            admins = HackAdmin.objects.order_by('user.first_name')
            persons = Person.objects.order_by('First_name')
            context = {
                'user': request.user,
                'success_message': 'New Admin successfully created',
                'admins': admins,
                'persons': persons,
            }
            return render(request, 'admin_home.html', context)
        else:
            context = {
                'error_message': 'Error in form submission, please check email provided!'
            }
    else:
        user_form = UserForm()
        hackAdmin_form = HackAdminForm()
        context = {
            'user_form':user_form,
            'hackAdmin_form':hackAdmin_form
        }
        return render (request, 'new_admin.html', context)
