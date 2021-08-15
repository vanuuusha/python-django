from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='advertisement_list'),
    path('advertisements/', views.ListAdvertisement.as_view(), name='advertisements'),
    path('сontacts/', views.Contacts.as_view(), name='contacts'),
    path('about/', views.About.as_view(), name='about'),
    path('advertisement/', views.RandomAdvertisement.as_view(), name='random_advertisement'),
    path('list_adv/', views.AdvertisementListView.as_view(), name='list_adv'),
    path('list_adv/<int:pk>', views.AdvertisementDetailView.as_view(), name='detail')
]
