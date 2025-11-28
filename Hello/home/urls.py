from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),

    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('flavour/', views.Flavour, name='flavour'),
    path('home/', views.Home, name='Home'),

    path('contact/', views.contactPage, name='contact'),
    path('contact/submit/', views.contactSubmit, name='contact_submit'),
]
