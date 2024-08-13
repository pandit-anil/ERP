from django.urls import path
from .views import *
urlpatterns = [
    path('inventory', InventoryView.as_view(), name ='inventory'),
]
