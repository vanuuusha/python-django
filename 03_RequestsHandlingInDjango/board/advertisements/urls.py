from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='advertisement_list'),
    path('advertisements/', views.ListAdvertisement.as_view(), name='advertisements'),
    path('сontacts/', views.Contacts.as_view(), name='contacts'),
    path('about/', views.About.as_view(), name='about')
]
