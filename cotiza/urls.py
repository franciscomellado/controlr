from django.urls import path
from . import views

urlpatterns = [
    path('', views.cotiza, name='cotiza'),
    path('', views.cliente, name='cliente'),
]
