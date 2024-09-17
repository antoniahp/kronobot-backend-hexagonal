from django.contrib import admin

from events.domain.competitor.competitor import Competitor
from events.domain.event.event import Event
from events.domain.inscription.inscription import Inscription

class EventAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "start_date",
        "category"
    ]

class CompetitorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]

class InscriptionAdmin(admin.ModelAdmin):
    list_display = [
        "get_pilot_name",
        "get_event_name",
        "car",
    ]

    def get_pilot_name(self, obj):
        return obj.pilot.name

    get_pilot_name.admin_order_field = 'pilot'

    def get_event_name(self, obj):
        return obj.event.name

    get_event_name.admin_order_field = 'event'


admin.site.register(Event, EventAdmin)
admin.site.register(Competitor, CompetitorAdmin)
admin.site.register(Inscription, InscriptionAdmin)

