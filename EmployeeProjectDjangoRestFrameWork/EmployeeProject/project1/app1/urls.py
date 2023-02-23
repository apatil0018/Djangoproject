from django.urls import path
from app1.views import EmployeeDetails, EmployeeInfo

urlpatterns = [
    path('emp/', EmployeeDetails.as_view()),
    path('emp/<int:id>/', EmployeeInfo.as_view()),
]