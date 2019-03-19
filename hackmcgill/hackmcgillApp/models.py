from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
import djongo

class User (AbstractUser):
    pass


# will be created with a User instantiation - only can be created when an admin is logged in
# view function that has admin creation form will have staff_required flag set beforehand
# FIRST ADMIN has to be done through createsuperuser command in django

roles = (
    ('Experience', 'Experience'),
    ('Development', 'Development'),
    ('Design', 'Design'),
    ('Communications', 'Communications'),
    ('Sponsorship', 'Sponsorship'),
    ('Logistics', 'Logistics'),
    ('Finance', 'Finance')
)

class HackAdmin (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')

    First_name = models.CharField(max_length=32)
    Last_name = models.CharField(max_length=32)
    Role = models.CharField(max_length=32, choices=roles)

class Person (models.Model):

    First_name = models.CharField(max_length=32)
    Last_name = models.CharField(max_length=32)
    Email = models.EmailField(max_length=256, unique=True)

