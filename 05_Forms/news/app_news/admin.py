from django.contrib import admin
from .models import News, Comment, NewsFlag


from .models import News, Comment, NewsFlag


class NewsFlagAdmin(admin.ModelAdmin):
    pass


class CommentsInLine(admin.TabularInline):
    model = Comment


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('author', )


class NewsAdmin(admin.ModelAdmin):
    inlines = [CommentsInLine]


admin.site.register(News, NewsAdmin)
admin.site.register(NewsFlag, NewsFlagAdmin)
admin.site.register(Comment, CommentAdmin)
