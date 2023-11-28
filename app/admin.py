from django.contrib import admin
from .models import Admission,Placements
# Register your models here.

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','phone','email','dob','address','place','course','qualification')

@admin.register(Placements)
class PlacementsAdmin(admin.ModelAdmin):
    list_display = ('images','name')