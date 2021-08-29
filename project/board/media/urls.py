from django.urls import path
from .views import FileView, FileCheckView


urlpatterns = [
    path('file/', FileView.as_view(), name='load-file'),
    path('file-check/', FileCheckView.as_view(), name='check-file' )
]