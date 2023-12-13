from django.contrib import admin
from django.utils import timezone

from .models import Issue

@admin.action(description='Close selected issues')
def close_issues(modeladmin, request, queryset):
    queryset.update(closed_at = timezone.now())

@admin.action(description='Reopen selected issues')
def reopen_issues(modeladmin, request, queryset):
    queryset.update(closed_at = None)

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
    actions = [close_issues, reopen_issues]
