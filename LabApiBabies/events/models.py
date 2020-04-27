from django.db import models
from datetime import datetime

# Create your models here.

class Baby(models.Model):
    # id creado por defecto
    eventType = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False, default=datetime.now)
    note = models.charField(max_length=200, null=False, blank=False)
    baby = models.ForeignKey('babies.Baby', on_delete=models.SET_NULL, null=False, blank=False)

    def __str__(self):
        return 'Event: {}'.format(self.eventType)
