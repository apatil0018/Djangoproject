from django.urls import path
from .views import CompanyListView, QualificationListView,WorkexpListView,ProjectListView

urlpatterns = [
    path('cmp/', CompanyListView.as_view()),
    path('exp/', WorkexpListView.as_view()),
    path('qual/',QualificationListView.as_view()),
    path('proj/',ProjectListView.as_view())

]