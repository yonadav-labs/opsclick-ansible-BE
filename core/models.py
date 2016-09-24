from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from mongoengine import *
from rest_framework.authtoken.models import Token
from django.conf import settings

class User(Document):
    username = StringField(max_length=20)
    password = StringField(max_length=20)
    token = StringField(max_length=128)

class Service(Document):
    name = StringField(max_length=50)

