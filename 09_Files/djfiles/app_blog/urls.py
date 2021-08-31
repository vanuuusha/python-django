from django.urls import path
from .views import ListBlogView, AddBlogView, DetailBlogView, AddBlogFile
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ListBlogView.as_view(), name="list-blog"),
    path('blog/<int:pk>/', DetailBlogView.as_view(), name='detail-blog'),
    path('add_blog/', AddBlogView.as_view(), name='add-block'),
    path('add_blog_file/', AddBlogFile.as_view(), name='add-block-file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)