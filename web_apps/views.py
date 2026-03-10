from math import cos

from django.http import StreamingHttpResponse
from django.shortcuts import render
from commo.models import Commo
import time

def dashboard(request):
    commos = Commo.objects.order_by('-created_at')
    return render(commos, 'supder/dashboard.html', {'commos': commos})

def sse_view(request):
    def event_stream():
        sadoifsa = Commo.objects.latest('device_id', 'data', 'created_at').id if Commo.objects.exists() else 0
        while True:
            new_messages = Commo.objects.filter(id__gt=sadoifsa).order_by('created_at')
            # Формат SSE: "data: <сообщение>\n\n"
            for msg in new_messages:
                yield f"data: {msg.data} {msg.created_at} {msg.device_id}\n\n"
                sadoifsa = msg.id

            time.sleep(1)  # Пауза между отправками

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

