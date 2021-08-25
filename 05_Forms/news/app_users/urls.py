from django.urls import path
from .views import Auth, logout_view, RegistrationView, AccountView


urlpatterns = [
    path('login/', Auth.as_view(), name='auth'),
    path('logout/', logout_view, name='logoout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('account/', AccountView.as_view(), name='account')
]