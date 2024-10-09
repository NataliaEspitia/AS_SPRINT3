from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_cobros, name='get_cobros'),
    path('<int:pk>', views.get_cobro, name='get_cobro')
]