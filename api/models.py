from django.db import models
from jsonfield import JSONField

# Create your models here.

class BlogPost(models.Model):
    body = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comments = JSONField(default={"all":[]})

    def __str__(self):
        return self.body[:50]