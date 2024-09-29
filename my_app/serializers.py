from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False, allow_blank=True)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return TodoItem(**validated_data).save() 

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance