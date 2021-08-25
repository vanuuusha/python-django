from django.contrib import admin
from .models import Comment, News


class CommentAdmin(admin.ModelAdmin):
    pass


class NewsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)
admin.site.register(News, NewsAdmin)
