from django.urls import path
from .views import *
urlpatterns = [
    path('accounting', AccountingView.as_view(), name ='accounting'),
]
