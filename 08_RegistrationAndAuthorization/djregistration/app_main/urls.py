from django.urls import path
from .views import MainView, ListNewsView, DetailNewsView, CreateNewsView, ModeratorView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('list-news/', ListNewsView.as_view(), name='list_news'),
    path('list-news/<int:pk>', DetailNewsView.as_view(), name='detail_news'),
    path('create-news', CreateNewsView.as_view(), name='create_new'),
    path('moderator-list-news/', ModeratorView.as_view(), name='moderator_url')
]