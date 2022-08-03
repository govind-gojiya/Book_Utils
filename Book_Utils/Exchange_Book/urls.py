from Exchange_Book import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('list', views.list, name="list"),
    path('selling', views.selling, name="selling"),
]