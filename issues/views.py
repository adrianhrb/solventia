from django.shortcuts import render

from .models import Issue


def opened_issues_list(request):
    issues = Issue.opened.all()
    return render(request, 'issues/opened.html', dict(issues=issues))


def closed_issues_list(request):
    issues = Issue.closed.all()
    return render(request, 'issues/closed.html', dict(issues=issues))
