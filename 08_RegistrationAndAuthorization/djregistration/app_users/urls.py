from django.urls import path
from .views import RegisterView, LogoutView, LoginView, ProfileView


urlpatterns = [
    path('registration/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile')
]