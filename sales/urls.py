from django.urls import path
from .views import IndexView, SalesView
urlpatterns = [
    path('index', IndexView.as_view(), name ='index'),
    path('sales', SalesView.as_view(), name ='sales'),

]
