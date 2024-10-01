from rest_framework import serializers
from .models import TodoItem
from .models import User

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
    

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email= validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user