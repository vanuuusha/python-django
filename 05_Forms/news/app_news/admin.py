from django.contrib import admin

from .models import News, Comment, NewsFlag


# Register your models here.
@admin.register(NewsFlag, News, Comment, )
class TotalAdmin(admin.ModelAdmin):
    pass
