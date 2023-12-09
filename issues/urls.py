from django.urls import path
from . import views

app_name = 'issues'

urlpatterns = [
    path('', views.opened_issues_list, name='opened'),
    path('closed/', views.closed_issues_list, name='closed'),
]
