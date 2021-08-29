from django.urls import path
from .views import UserLogin, UserRegister, LogoutView, AccountView

urlpatterns = [
    path('login/', UserLogin.as_view(), name='user-login'),
    path('register/', UserRegister.as_view(), name='user-register'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('account/', AccountView.as_view(), name="account"),
]