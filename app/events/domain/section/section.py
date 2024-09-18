import uuid

from django.db import models

from events.domain.event.event import Event


class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
