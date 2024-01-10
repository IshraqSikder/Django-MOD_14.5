from django.urls import path
from . import views

urlpatterns = [
    path('bootstrap_form/', views.forms, name= 'forms'),
    path('django_form/', views.djangoForm, name= 'djangoForm'),
]