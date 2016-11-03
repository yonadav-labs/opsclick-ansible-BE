from django.db import models
from django.conf import settings
from django_mongoengine import Document, fields, EmbeddedDocument
from datetime import datetime

class User(Document):
    username = fields.StringField(max_length=20)
    password = fields.StringField(max_length=20)
    token = fields.StringField(max_length=128)

class Addon(Document):
    name = fields.StringField(unique_with=['type', 'version'])
    type = fields.StringField(choices=('cloud', 'service'))
    category = fields.StringField()
    author = fields.StringField()
    version = fields.StringField()
    depends = fields.ListField(fields.StringField(blank=True), default=['core'])
    clouds = fields.ListField(fields.StringField(blank=True), default=['core'])
    fields = fields.ListField(fields.DictField())

class Key(Document):
    user = fields.StringField()
    cloud = fields.StringField()
    private = fields.StringField()
    public = fields.StringField()

class AnsibleTask(EmbeddedDocument):
    hosts = fields.DictField()
    task = fields.DictField()

class AnsiblePlay(EmbeddedDocument):
    play = fields.DictField()
    tasks = fields.ListField(fields.EmbeddedDocumentField(AnsibleTask, blank=True))

class AnsiblePlaybook(Document):
    plays = fields.ListField(fields.EmbeddedDocumentField(AnsiblePlay, blank=True))
    stats = fields.DictField()
    created_at = fields.DateTimeField(default=datetime.now)

class Options(EmbeddedDocument):
    access_key = fields.StringField()
    droplets = fields.ListField(fields.StringField())
    ssh_pub_keys = fields.ListField(fields.DictField())
    size = fields.StringField()
    region = fields.StringField()
    image = fields.StringField()
    state = fields.StringField()
    service_opts = fields.DictField(default={'core': 'core'})

class Setup(Document):
    user = fields.StringField(max_length=50)
    service = fields.StringField(max_length=50)
    cloud = fields.StringField(max_length=50)
    options = fields.EmbeddedDocumentField(Options, blank=True)
    playbook = fields.ObjectIdField(blank=True)
    key_id = fields.ObjectIdField(blank=True)
    status = fields.StringField()
