import uuid

from django.db import models

from events.domain.event.event import Event


class Competitor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to="events", blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="competitors")
