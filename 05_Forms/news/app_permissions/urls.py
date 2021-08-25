from django.urls import path
from .views import ListVacancyView


urlpatterns = [
    path('list_vacancy/', ListVacancyView.as_view(), name='list_vacancy')
]