from django import forms
from .models import Issue

class CreateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'queue', 'urgent']