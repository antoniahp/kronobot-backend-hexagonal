from django.contrib import admin

from events.domain.competitor.competitor import Competitor
from events.domain.event.event import Event
from events.domain.inscription.inscription import Inscription
from events.domain.section.section import Section
from events.domain.section_time.section_time import SectionTime


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


class SectionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "code"
    ]

class SectionTimeAdmin(admin.ModelAdmin):
    list_display = [
        "get_event_name",
        "get_section_name",
        "get_pilot_name",
        "section_time"
    ]

    def get_section_name(self, obj):
        return obj.section.name

    get_section_name.admin_order_field = 'section'

    def get_pilot_name(self, obj):
        return obj.inscription.pilot.name

    get_pilot_name.admin_order_field = 'pilot_name'

    def get_event_name(self, obj):
        return obj.section.event.name

    get_pilot_name.admin_order_field = 'pilot_name'

admin.site.register(Event, EventAdmin)
admin.site.register(Competitor, CompetitorAdmin)
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(SectionTime, SectionTimeAdmin)

