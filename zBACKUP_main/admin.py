from django.contrib import admin

from .models import ft_Company, ft_Place, ft_Event, ft_Worker
# Register your models here.


@admin.register(ft_Worker)
class ft_Worker_Admin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number")


@admin.register(ft_Company)
class ft_Company_Admin(admin.ModelAdmin):
    list_display = ("name")


@admin.register(ft_Place)
class ft_Place_Admin(admin.ModelAdmin):
    list_display = ("name", "region")


@admin.register(ft_Event)
class ft_Event_Admin(admin.ModelAdmin):
    list_display = ("name", "place")
