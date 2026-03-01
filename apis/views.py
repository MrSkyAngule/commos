from rest_framework import permissions, viewsets

from apis.serializers import CommoSerializer
from commo.models import Commo


class send_Views(viewsets.ModelViewSet):
    serializer_class = CommoSerializer
    queryset = Commo.objects.all().order_by('-created_at')

