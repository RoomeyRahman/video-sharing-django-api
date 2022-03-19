from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200, null=True, blank=True)
    creator = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
      return self.title