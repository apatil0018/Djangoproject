from django.urls import path
from .import views

urlpatterns = [
    path('of/',views.orderFormView,name='addorder_url'),
    path('so/',views.showOrdersView, name='showorder_url'),
    path('uo/<int:id>/',views.updateOrdersView,name='updateorder_url'),
    path('dl<int:id>/',views.deleteOrderView,name='deleteorder_url'),
    
]
