from django.urls import path
from app1.views import StudentDetails

urlpatterns = [
    path('std/',StudentDetails.as_view()),
    
]
