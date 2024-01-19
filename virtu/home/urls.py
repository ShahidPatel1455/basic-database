from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', home),
    path('post_data', post_data),
    path('index',views.index,name="index")
]