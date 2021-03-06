from django.urls import path
from accounts.views import Home
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'),
         name = 'login'),
    path('login/', auth_views.LogoutView.as_view(template_name='base/login.html'),
         name = 'logout'),
]
