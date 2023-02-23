from django.urls import path
from app1 import views

urlpatterns = [
    path('resume/',views.ProfileView.as_view(),name='resume'),
    path('list/',views.ProfileView.as_view(),name='list')
]
