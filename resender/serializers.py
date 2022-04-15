from rest_framework import serializers
from resender.models import Dialog


class DialogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dialog
        fields = "__all__"
