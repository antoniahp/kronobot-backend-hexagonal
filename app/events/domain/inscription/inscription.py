import uuid

from django.db import models

from events.domain.competitor.competitor import Competitor
from events.domain.event.event import Event



class Inscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='inscription_event')
    car = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    dorsal = models.CharField(max_length=12)
    pilot = models.ForeignKey(Competitor, on_delete=models.CASCADE, related_name='inscription_pilot')
    copilot = models.ForeignKey(Competitor, on_delete=models.CASCADE, related_name='inscription_copilot', null=True, blank=True)
