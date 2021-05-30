from django.contrib import admin
from django.template.defaultfilters import escape
from django.urls import reverse

from .models import ft_Company, ft_Place, ft_Event, ft_Worker
# Register your models here.


@admin.register(ft_Worker)
class ft_Worker_Admin(admin.ModelAdmin):
    list_display = ["get_name", "phone_number"]
    fields = ["first_name", "last_name", "gender", "phone_number",
              "email", "bank_account_number", "username"]

    def get_name(self, obj):
        if obj.first_name and obj.last_name:
            return obj.first_name + " " + obj.last_name
        else:
            return 'Jméno nenalezeno!'

    get_name.short_description = 'Jméno'


@admin.register(ft_Company)
class ft_Company_Admin(admin.ModelAdmin):
    list_display = ["get_name"]

    def get_name(self, obj):
        if obj.name:
            return obj.name
        else:
            return 'Neznámé Jméno'

    get_name.short_description = 'Jméno'


@admin.register(ft_Place)
class ft_Place_Admin(admin.ModelAdmin):
    list_display = ["name", "region"]
    list_filter = ["region", ]


@admin.register(ft_Event)
class ft_Event_Admin(admin.ModelAdmin):
    list_display = ["name", "place", "show_total_price",
                    "show_expenses", "show_profit", "show_place", "show_workers"]
    list_filter = ["place", ]

    def show_total_price(self, obj):
        if obj.total_meters and obj.czk_per_meter:
            return str(int(obj.total_meters * obj.czk_per_meter)) + ' Kč'
        else:
            return 'Nedostatek informací! (error)'

    show_total_price.short_description = 'Celková cena'

    def show_expenses(self, obj):
        if obj.total_meters and obj.czk_per_meter:
            return str(int(obj.total_meters * 450)) + ' Kč'
        else:
            return 'Nedostatek informací! (error)'

    show_expenses.short_description = 'Výdaje'

    def show_profit(self, obj):
        if obj.total_meters and obj.czk_per_meter:
            return (int(obj.total_meters * obj.czk_per_meter) - int(obj.total_meters * 450))
        else:
            return 'Nedostatek informací! (error)'

    show_profit.short_description = 'Čistý zisk'

    def show_place(self, obj):
        if obj.place.name:
            return obj.place.name
        else:
            return "Místo nenalezeno."

    show_place.short_description = 'Místo'

    def show_workers(self, obj):
        result = ""
        if obj.workers.all():
            for worker in obj.workers.all():
                # result += '<a href="%s">%s</a>' % (reverse("admin:auth_user_change", args=(
                # worker.id,)), escape(worker.first_name + " " + worker.last_name))
                result += worker.first_name + " " + worker.last_name + "<br>"
        return result
    show_workers.short_description = 'Vrtači'
    show_workers.allow_tags = True

    '''
    def view_workers(self, obj):
        count = obj.ft_workers_set.count()
        return count


    def view_students_link(self, obj):
        count = obj.person_set.count()
        url = (
            reverse("admin:core_person_changelist")
            + "?"
            + urlencode({"courses__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Students</a>', url, count)

    view_students_link.short_description = "Students"
    '''
