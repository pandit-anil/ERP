from django.shortcuts import render
from django.views.generic import TemplateView

class HRView(TemplateView):
    template_name =  'hr.html'