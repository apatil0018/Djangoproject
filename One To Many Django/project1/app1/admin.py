from django.contrib import admin
from .models import Student,Courses

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['rn','fname','lname','city']

admin.site.register(Student,StudentAdmin)

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id','student','courseName']

admin.site.register(Courses,CoursesAdmin)

