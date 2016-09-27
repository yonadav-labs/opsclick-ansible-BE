from rest_framework import serializers
from core.models import User, Service, Setup

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

class SetupSerializer(serializers.Serializer):
    service = serializers.CharField()
    cloud = serializers.CharField()

    def create(self, validated_data):
        return Setup.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.service = validated_data.get('service', instance.service)
        instance.cloud = validated_data.get('cloud', instance.cloud)
        instance.save()
        return instance

