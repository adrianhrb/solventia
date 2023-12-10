from django.shortcuts import render, redirect
from django.core.mail import send_mail
from prettyconf import config

from .models import Issue
from .forms import CreateIssueForm


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