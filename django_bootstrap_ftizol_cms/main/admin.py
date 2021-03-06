from django.contrib import admin
from django.template.defaultfilters import escape
from django.urls import reverse
from django.utils.safestring import mark_safe
import unidecode


from .models import ft_Company, ft_Place, ft_Event, ft_Worker, ft_Upcoming_Event
# Register your models here.

# ft_Worker
# the most essential part of this, also has all the personal info of workers
#


@admin.register(ft_Worker)
class ft_Worker_Admin(admin.ModelAdmin):
    list_display = ["get_name", "get_call_phone",
                    "bank_account_number"]
    fields = ["first_name", "last_name", "display_name", "gender", "phone_number",
              "email", "bank_account_number", "username", "password", "date_of_birth", "power"]

    search_fields = ["first_name", "last_name", "gender", "phone_number",
                     "email", "bank_account_number", "username"]

   # readonly_fields = ('password', )

    def get_name(self, obj):
        username = obj.last_name[0:6] + obj.first_name[0]
        if obj.first_name and obj.last_name:
            return obj.first_name + " " + obj.last_name + " / " + unidecode.unidecode(username).lower()
        else:
            return 'Jméno nenalezeno!'

    get_name.short_description = 'Jméno'

    def get_display_name(self, obj):
        username = obj.last_name[0:6] + obj.first_name[0]
        if obj.first_name and obj.last_name:
            return obj.first_name + " " + obj.last_name + " / " + unidecode.unidecode(username).lower()
        else:
            return 'Jméno nenalezeno!'

    get_display_name.short_description = 'Jméno'

    def get_call_phone(self, obj):
        phone_number = str(obj.phone_number)
        result = "Neznámý tel."
        if(phone_number == "None"):
            return result
        if(phone_number.startswith("+")):
            result = '<a href="tel:' + phone_number + '">' + phone_number + '</a>'
        else:
            # <a href="tel:5554280940"></a>
            result = '<a href="tel:+420' + phone_number + \
                '">' + '+420 ' + phone_number + '</a>'

        return mark_safe(result)

    get_call_phone.allow_tags = True
    get_call_phone.short_description = "Tel. číslo"

# ft_Company
# References a company we work(ed) with


@admin.register(ft_Company)
class ft_Company_Admin(admin.ModelAdmin):
    list_display = ["get_name"]

    def get_name(self, obj):
        if obj.name:
            return obj.name
        else:
            return 'Neznámé Jméno'

    get_name.short_description = 'Jméno'

# ft_Place
# References a town and a region


@admin.register(ft_Place)
class ft_Place_Admin(admin.ModelAdmin):
    list_display = ["name", "region"]
    list_filter = ["region", ]

# ft_Event
# Already passed event
# used for calculating profits and keeping track of workers


def add_thousand_separator(number):
    result = ""
    loop_string = str(number)
    index = 0
    total_numbers = 0
    for number in loop_string:
        result += number
        index += 1
        total_numbers += 1
        if index == 3 and total_numbers != len(loop_string):
            result += ","
            index = 0

    return result


@admin.register(ft_Event)
class ft_Event_Admin(admin.ModelAdmin):
    list_display = ["name", "place", "show_workers", "show_total_price",
                    "show_expenses", "show_profit", ]
    list_filter = ["place"]

    def show_total_price(self, obj):
        if obj.total_meters and obj.czk_per_meter:
            return add_thousand_separator(int(obj.total_meters * obj.czk_per_meter)) + ' Kč'
        else:
            return 'Nedostatek informací! (error)'

    show_total_price.short_description = 'Celková cena'

    def show_expenses(self, obj):

        if obj.total_meters and obj.czk_per_meter:
            return add_thousand_separator((int(obj.total_meters * 450))) + ' Kč'
        else:
            return 'Nedostatek informací! (error)'

    show_expenses.short_description = 'Výdaje'

    def show_profit(self, obj):
        if obj.total_meters and obj.czk_per_meter:
            return add_thousand_separator(int(obj.total_meters * obj.czk_per_meter) - int(obj.total_meters * 450)) + " Kč"
        else:
            return 'Nedostatek informací! (error)'

    show_profit.short_description = 'Čistý zisk'

    def show_workers(self, obj):
        result = ""
        if obj.workers.all():
            for worker in obj.workers.all():
                # result += '<a href="%s">%s</a>' % (reverse("admin:auth_user_change", args=(
                # worker.id,)), escape(worker.first_name + " " + worker.last_name))
                result += worker.first_name + " " + worker.last_name + "<br>"
        return mark_safe(result)
    show_workers.short_description = 'Vrtači'
    show_workers.allow_tags = True


# ft_Upcoming_Event
# An upcoming event to which a worker can sign up to

@admin.register(ft_Upcoming_Event)
class ft_Event_Admin(admin.ModelAdmin):
    list_display = ["name", "place", "count_workers",  "show_workers",
                    "show_capacity", "total_meters"]
    list_filter = ["place", "start_month", "year"]

    fields = ["name", "start_date", "end_date", "description",
              "place", "total_meters", "wall_type", "workers_required", "workers_ready"]

    readonly_fields = ["workers_required", ]

    search_fields = ["name", "last_name", "display_name", "gender", "phone_number",
                     "email", "bank_account_number", "username", "password", "date_of_birth"]

    def count_workers(self, obj):
        result = 0
        if obj.workers_ready.all():
            for worker in obj.workers_ready.all():
                result += 1
        return mark_safe(result)
    count_workers.short_description = "#    "

    def show_workers(self, obj):
        result = ""
        if obj.workers_ready.all():
            for worker in obj.workers_ready.all():
                result += worker.first_name + " " + worker.last_name + "<br>"
        return mark_safe(result)
    show_workers.short_description = 'Dostupní Vrtači'
    show_workers.allow_tags = True

    def show_capacity(self, obj):
        result = ""
        workers_req = int(obj.workers_required)
        workers_ready = int(obj.workers_ready.count())
        if obj.workers_ready.count() != 0 and workers_req > workers_ready:
            result = "<b>" + str(obj.workers_ready.count()) + " / " + \
                str(obj.workers_required) + "</b>"
        else:
            result = str(obj.workers_ready.count()) + " / " + \
                str(obj.workers_required)

        return mark_safe(result)

    show_capacity.short_description = 'Kapacita'
    show_capacity.allow_tags = True

    class Meta:
        ordering = ['workers_ready']  # Sort in asc order

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
