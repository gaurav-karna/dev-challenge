# from django.db import models
from djongo import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# sign in will be via username and password - validation done by Django validators.
class User (AbstractUser):
    pass

roles = (
    ('Experience', 'Experience'),
    ('Development', 'Development'),
    ('Design', 'Design'),
    ('Communications', 'Communications'),
    ('Sponsorship', 'Sponsorship'),
    ('Logistics', 'Logistics'),
    ('Finance', 'Finance')
)

# will be created with a User instantiation - only can be created when an admin is logged in
# view function that has admin creation form will have staff_required flag set beforehand
# FIRST ADMIN has to be done through createsuperuser command in django
class HackAdmin (models.Model):
    objects = models.DjongoManager()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')

    Role = models.CharField(max_length=32, choices=roles)


# visitor object - will sign up via public email form on index page.
class Person (models.Model):
    objects = models.DjongoManager()
    First_name = models.CharField(max_length=32)

    Last_name = models.CharField(max_length=32)

    Email = models.EmailField(max_length=256, unique=True)

