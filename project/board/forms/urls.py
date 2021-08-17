from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('reg/', views.UserFormView.as_view(), name='reg')
]
