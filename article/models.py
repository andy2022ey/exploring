from django.db import models
from django.utils import timezone

class Item(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

