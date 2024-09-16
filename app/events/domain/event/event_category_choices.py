from django.db import models
class EventCategoryChoices(models.TextChoices):
    RALLY = "RALLY"
    HILL_CLIMB = "HILL-CLIMB"
    AUTO_CROSS = "AUTO-CROSS"
    KARTING = "KARTING"