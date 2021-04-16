from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('view', views.view, name='view'),


]
