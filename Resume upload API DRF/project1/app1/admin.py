from django.contrib import admin
from app1.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','name','email','dob','state','gender','location','pimage','rdoc']

admin.site.register(Profile,ProfileAdmin)
