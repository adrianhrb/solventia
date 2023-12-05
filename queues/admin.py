from django.contrib import admin

from .models import Queue


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'color', 'email_to']
    prepopulated_fields = {'slug': ['name']}
