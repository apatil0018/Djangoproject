from django.urls import path
from .import views

urlpatterns = [
    path('sf/',views.studentView, name='studentformurl'),
    path('cf/',views.coursesView, name='courseformurl'),
    path('ss/',views.showStudent,name='studentdataurl'),
    path('sc/',views.showCourses,name='coursedataurl'),
    
]