from django.contrib import admin
from .models import News, Comment, NewsFlag


class NewsFlagAdmin(admin.ModelAdmin):
    pass


class CommentsInLine(admin.TabularInline):
    model = Comment


class CommentAdmin(admin.ModelAdmin):
    actions = ['admin_delete']

    def admin_delete(self, request, queryset):
        queryset.update(content='Удалено администратором')

    admin_delete.short_description = 'Удалить от имени администратора'

    def get_content(self, obj):
        return f'{obj.content}' if len(obj.content) < 15 else ''.join([f'{obj.content[:15]}', '...'])

    list_filter = ('author', )
    list_display = ('author', 'get_content')


class NewsAdmin(admin.ModelAdmin):
    actions = ['mark_as_active', 'mark_as_unactive']

    def mark_as_active(self, request, queryset):
        now_flag = NewsFlag.objects.get(name='активно')
        queryset.update(flag=now_flag)

    def mark_as_unactive(self, request, queryset):
        now_flag = NewsFlag.objects.get(name='неактивно')
        queryset.update(flag=now_flag)

    mark_as_active.short_description = 'Сделать активными'
    mark_as_unactive.short_description = 'Сделать не активными'

    list_filter = ('flag', )
    inlines = [CommentsInLine]
    list_display = ('id', 'name', 'date_make', 'date_corrected', 'flag')


admin.site.register(News, NewsAdmin)
admin.site.register(NewsFlag, NewsFlagAdmin)
admin.site.register(Comment, CommentAdmin)
