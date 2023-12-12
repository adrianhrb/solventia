from django.db import models
from django.urls import reverse

from .utils import get_random_rgb


class Queue(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    color = models.CharField(max_length=13, blank=True, default=get_random_rgb)
    email_to = models.EmailField()

    def save(self, *args, **kwargs):
        if not self.color:
            self.color = get_random_rgb()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('queues:detail', args=[self.id])
