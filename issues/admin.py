from django.contrib import admin

from .models import Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'queue',
        'urgent',
        'created_at',
        'updated_at',
        'closed_at',
    ]
    raw_id_fields = ['queue']
