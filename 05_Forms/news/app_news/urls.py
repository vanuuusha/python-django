from django.urls import path
from .views import ListNews, DetailNews, AddNews, Main


urlpatterns = [
    path('list-news/', ListNews.as_view(), name='list_news'),
    path('list-news/<int:pk>', DetailNews.as_view(), name='detail_news'),
    path('add-news/', AddNews.as_view(), name='add_new'),
    path('', Main.as_view(), name='main')
]
