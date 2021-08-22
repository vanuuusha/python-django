from django.urls import path
from .views import Auth, logout_view


urlpatterns = [
    path('login/', Auth.as_view(), name='auth'),
    path('logout/', logout_view, name='logoout')
]