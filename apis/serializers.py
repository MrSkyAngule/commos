from rest_framework import serializers

from commo.models import Commo


class CommoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commo
        fields = ['device_id', 'data']