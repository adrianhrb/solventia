from django.urls import path

from . import views

app_name = 'queues'

urlpatterns = [
    path('<int:queue_id>', views.queue_detail, name='detail'),
]
