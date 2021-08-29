from django.urls import path
from .views import GoodsList, GoodsLoad


urlpatterns = [
    path('', GoodsList.as_view(), name='goods-list'),
    path('load/', GoodsLoad.as_view(), name='goods-load'),
]