from django.urls import path
from . import views

urlpatterns = [
    path('advertisements/', views.AdverisementList.as_view(), name='list_adv'),
    path('advertisements/<int:pk>', views.AdvertisementDetail.as_view(), name='detail'),
]
