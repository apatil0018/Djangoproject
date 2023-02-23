from django.urls import path
from .import views

urlpatterns = [
    path('ov/',views.ownerView, name='addown_url'),
    path('cv/',views.carView, name='addcrs_url'),
    path('sw/',views.showownView,name="show_own_url"),
    path('sc/',views.showcarView,name='show_car_url'),
    path('uw/<int:id>/',views.updateownView,name='updateown_url'),
    path('uc/<int:id>/',views.updatecarView,name='updatecar_url'),
    
    path('dw/<int:id>',views.deleteownView,name='delete_own_url'),
    path('dc/<int:id>',views.deletecarView,name='del_url'),
    

    





]