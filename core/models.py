from django.db import models
from rest_framework.authtoken.models import Token
from django.conf import settings
from django_mongoengine import Document, fields, EmbeddedDocument

class User(Document):
    username = fields.StringField(max_length=20)
    password = fields.StringField(max_length=20)
    token = fields.StringField(max_length=128)

class Service(Document):
    name = fields.StringField(max_length=50)

class AnsiblePlay(EmbeddedDocument):
    play = fields.DictField()
    tasks = fields.ListField(fields.DictField())

class AnsiblePlaybook(Document):
#    plays = fields.ListField(fields.EmbeddedDocumentField(AnsiblePlay, required=False))
    plays = fields.ListField(fields.DictField())
    stats = fields.DictField()

class Options(EmbeddedDocument):
    access_key = fields.StringField()
    droplets = fields.ListField(fields.StringField(required=False))
    ssh_pub_key = fields.StringField()
    size = fields.StringField()
    region = fields.StringField()
    image = fields.StringField()
    state = fields.StringField()

class Setup(Document):
    service = fields.StringField(max_length=50)
    cloud = fields.StringField(max_length=50)
    options = fields.EmbeddedDocumentField(Options, required=False)
    tasklist = fields.ObjectIdField()
