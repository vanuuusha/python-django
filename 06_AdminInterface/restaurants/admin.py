from django.contrib import admin
from .models import Restaurant, Waiter


class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Личная информация', {
            'fields': ('name', 'description', 'phone', 'country', 'city', 'street', 'house')
                               }),
        ('Сервисы', {
            'fields': ('serves_hot_dogs', 'serves_pizza', 'serves_sushi', 'serves_burgers', 'serves_donats', 'serves_coffee')
        }),
        ('Информация по месту работы', {
            'fields': ('count_of_employers', 'director', 'chef')
        })
    )


class WaiterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Waiter, WaiterAdmin)

