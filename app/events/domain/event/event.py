import uuid
from datetime import date

from django.db import models
from ckeditor.fields import RichTextField

from events.domain.event.event_category_choices import EventCategoryChoices
from events.domain.event.event_provider_choices import EventProviderChoices


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    event_external_id = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    picture = models.ImageField(upload_to="events", blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=16,choices=EventCategoryChoices.choices,)
    provider_name = models.CharField( max_length=16, choices=EventProviderChoices.choices, default=EventProviderChoices.KRONOBOT)
    provider_data = models.JSONField(default=dict, blank=True)

    def is_live(self):
        return self.start_date <= date.today() <= self.end_date

    def __str__(self) -> str:
        return self.name