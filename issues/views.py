from django.shortcuts import render, redirect
from django.core.mail import send_mail
from prettyconf import config
from django.utils import timezone

from .models import Issue
from .forms import CreateIssueForm, EditIssueForm


def opened_issues_list(request):
    issues = Issue.opened.all()
    return render(request, 'issues/opened.html', dict(issues=issues, section='abiertas'))


def closed_issues_list(request):
    issues = Issue.closed.all()
    return render(request, 'issues/closed.html', dict(issues=issues, section='cerradas'))

def issue_detal(request, issue_id: int):
    issue = Issue.objects.get(id=issue_id)
    return render(request, 'issues/detail.html', dict(issue=issue))

def open_new_issue(request):
    if request.method == 'POST':
        form = CreateIssueForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            subject = cd['title']
            message = cd['description']
            from_mail = config('EMAIL_HOST_USER')
            to_mail = cd['queue'].email_to
            send_mail(subject, message, from_mail, [to_mail])
            return redirect('issues:opened')
    else:
        form = CreateIssueForm()
        return render(request, 'issues/create.html', dict(form=form, section='crear'))

def edit_issue(request, issue_id: int):
    issue = Issue.objects.get(id=issue_id)
    if request.method == 'POST':
        form = EditIssueForm(request.POST, instance=issue)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            subject = f'{cd["title"]} se ha editado'
            message = cd['description']
            from_mail = config('EMAIL_HOST_USER')
            to_mail = cd['queue'].email_to
            send_mail(subject, message, from_mail, [to_mail])
            return redirect('issues:opened')
    else:
        form = EditIssueForm(instance=issue)
        return render(request, 'issues/edit.html', dict(form=form))

def close_issue(request, issue_id: int):
    issue = Issue.objects.get(id=issue_id)
    issue.closed_at = timezone.now()
    issue.save()
    return redirect('issues:closed')

def reopen_issue(request, issue_id: int):
    issue = Issue.objects.get(id=issue_id)
    issue.closed_at = None
    issue.save()
    return redirect('issues:opened')