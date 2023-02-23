from django.contrib import admin
from .models import Person,Adhar

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['pid','fname','lname']

admin.site.register(Person,PersonAdmin)

class AdharAdmin(admin.ModelAdmin):
    list_display = ['person','adharno']

admin.site.register(Adhar,AdharAdmin)
