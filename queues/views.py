from django.shortcuts import render
from .models import Queue

def queue_list(request):
    queues = Queue.objects.all()
    return render(request, 'queues/list.html', dict(queues=queues))

def queue_detail(request, queue_id: int):
    queue = Queue.objects.get(id=queue_id)
    return render(request, 'queues/detail.html', dict(queue=queue))


