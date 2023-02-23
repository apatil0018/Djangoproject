from django.urls import path
from .import views

urlpatterns =[
    path('pv/',views.personView,name='personurl'),
    path('av/',views.adharView,name='adharurl'),
    path('shp/',views.showPerson,name='showpersonurl'),
    path('sha/',views.showAdhar, name='showadharurl'),
    
]