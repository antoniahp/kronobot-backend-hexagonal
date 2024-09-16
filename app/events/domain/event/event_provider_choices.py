from django.db import models
class EventProviderChoices(models.TextChoices):
    KRONOLIVE = "KRONOLIVE"
    KRONOBOT = "KRONOBOT"
