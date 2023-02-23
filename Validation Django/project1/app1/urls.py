from django.urls import path
from .import views

urlpatterns = [
    path('ev/',views.electionView),
]