from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.stuView,name='add'),
    path('list/<int:roll_no>/',views.ResultList,name='list'),


]