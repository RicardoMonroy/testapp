from rest_framework import serializers
from .models import Tasks

class TaskSerialaizer(serializers.ModelSerializer):
    class Meta:
        model: Tasks
        exclude = ('created_at', 'updated_at')