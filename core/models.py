from django.db import models
from rest_framework.authtoken.models import Token
from django.conf import settings
from django_mongoengine import Document, EmbeddedDocument, fields

class User(Document):
    username = fields.StringField(max_length=20)
    password = fields.StringField(max_length=20)
    token = fields.StringField(max_length=128)

class Service(Document):
    name = fields.StringField(max_length=50)

