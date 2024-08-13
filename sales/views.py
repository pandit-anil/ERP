from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name =  'index.html'
    
class SalesView(TemplateView):
    template_name =  'sales.html'
    
