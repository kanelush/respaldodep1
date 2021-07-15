from django.db import models
from datetime import datetime as dt
import datetime

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=datetime.datetime.now, blank=True,null=True)

    def __str__(self):
        return self.subject