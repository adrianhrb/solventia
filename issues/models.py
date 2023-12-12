from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse

from queues.models import Queue


class OpenedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(closed_at=None)


class ClosedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().exclude(closed_at=None)


class Issue(models.Model):
    queue = models.ForeignKey(Queue, related_name='issues', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    urgent = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    opened = OpenedManager()
    closed = ClosedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('issues:detail', args=[self.id])
