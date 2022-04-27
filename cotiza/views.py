from django.shortcuts import render
from django.template import Template

# Create your views here.
def cotiza(request):
    return render(request, 'cotiza/cotiza.html')

