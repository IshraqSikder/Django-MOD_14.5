from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.forms, name = "form"),
    path('delete/<int:roll>', views.delete_model, name = "delete"),
]