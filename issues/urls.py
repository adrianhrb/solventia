from django.urls import path
from . import views

app_name = 'issues'

urlpatterns = [
    path('', views.opened_issues_list, name='opened'),
    path('closed/', views.closed_issues_list, name='closed'),
    path('create/', views.open_new_issue, name='create'),
    path('<int:issue_id>', views.issue_detal, name='detail'),
    path('edit/<int:issue_id>', views.edit_issue, name='edit')
]
