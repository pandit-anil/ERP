from django.urls import path
from .views import *
urlpatterns = [
        path('hr', HRView.as_view(), name ='hr'),
]
