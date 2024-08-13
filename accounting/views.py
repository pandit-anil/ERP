from django.shortcuts import render
from django.views.generic import TemplateView

    
class AccountingView(TemplateView):
    template_name =  'accounting.html'
    
