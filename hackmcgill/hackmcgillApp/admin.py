from django.contrib import admin

from .models import User, Person, HackAdmin

# Register your models here.

admin.site.register([User, HackAdmin, Person])
