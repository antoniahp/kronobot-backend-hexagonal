import uuid

from django.db import models

from events.domain.inscription.inscription import Inscription
from events.domain.section.section import Section


class SectionTime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    section_time = models.DurationField()
