from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('view', views.view, name='view'),
    path('change_status', views.change_status, name='change_status'),
    path('block', views.block, name='block'),
    path('ledger', views.ledgder, name='ledger'),


]
