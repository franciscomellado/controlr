from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base/base.html'
    login_url = '/admin'


def ordenes(request):
    return HttpResponse("ordenes")


