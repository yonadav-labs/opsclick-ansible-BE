from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer

from core.models import User, Service, Setup, Options, AnsiblePlaybook, AnsiblePlay, AnsibleTask

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

class AnsibleTaskSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = AnsibleTask
        fields = ('hosts', 'task')

class AnsiblePlaySerializer(EmbeddedDocumentSerializer):
    tasks = AnsibleTaskSerializer(many=True)

    class Meta:
        model = AnsiblePlay
        fields = ('play', 'tasks')

class AnsiblePlaybookSerializer(DocumentSerializer):
    plays = AnsiblePlaySerializer(many=True)

    def create(self, validated_data):
        return AnsiblePlaybook.objects.create(**validated_data)

    class Meta:
        model = AnsiblePlaybook
        fields = ('plays', 'stats')

class OptionsSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Options
        fields = '__all__'

class SetupSerializer(DocumentSerializer):
    options = OptionsSerializer(many=False)

    def create(self, validated_data):
        return Setup.objects.create(**validated_data)

    class Meta:
        model = Setup
        fields = ('service', 'cloud', 'options')

