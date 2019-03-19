from django.contrib import admin

from .models import User, Person, HackAdmin
# from .models import Person, HackAdmin

# Register your models here.

admin.site.register([User, HackAdmin, Person])
# admin.site.register([HackAdmin, Person])