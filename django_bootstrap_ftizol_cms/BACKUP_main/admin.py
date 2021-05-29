from django.contrib import admin

from .models import ft_Company, ft_Place, ft_Event, ft_Worker
# Register your models here.

admin.site.register(ft_Worker)
admin.site.register(ft_Company)
admin.site.register(ft_Place)
admin.site.register(ft_Event)
