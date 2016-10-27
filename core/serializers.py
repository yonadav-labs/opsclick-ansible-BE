#from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from django_mongoengine import fields
from core.models import User, Addon, Setup, Options, AnsiblePlaybook, AnsiblePlay, AnsibleTask

# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#     token = serializers.CharField(required=False)

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('username', instance.title)
#         instance.code = validated_data.get('password', instance.code)
#         instance.save()
#         return instance


class AddonSerializer(DocumentSerializer):
    class Meta:
        model = Addon
        fields = '__all__'

    def create(self, validated_data):
        return Addon.objects.create(**validated_data)

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
    service_opts = fields.DictField(required=False)

    class Meta:
        model = Options
        fields = '__all__'


class SetupSerializer(DocumentSerializer):
    options = OptionsSerializer(many=False)

    def create(self, validated_data):
        return Setup.objects.create(**validated_data)

    class Meta:
        model = Setup
        fields = ('user', 'service', 'cloud', 'options')

