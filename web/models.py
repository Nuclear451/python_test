from django.db import models
from django.utils import timezone


class Post(models.Model):
    text = models.TextField()
    post_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.post_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
