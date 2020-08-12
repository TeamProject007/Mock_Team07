from django.contrib import admin

# Register your models here.
from .models import Donor,Donee,Item,Requirement
admin.site.register(Donor)
admin.site.register(Donee)
admin.site.register(Item)
admin.site.register(Requirement)
