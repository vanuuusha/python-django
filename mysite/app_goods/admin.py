from django.contrib import admin
from .models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price')


admin.site.register(Goods, GoodsAdmin)