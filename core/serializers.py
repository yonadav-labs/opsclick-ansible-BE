from rest_framework import serializers
from core.models import User, Service

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('username', instance.title)
        instance.code = validated_data.get('password', instance.code)
        instance.save()
        return instance

class ServiceSerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return Service.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
