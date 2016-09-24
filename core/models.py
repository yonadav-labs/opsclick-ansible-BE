from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from mongoengine import *
from rest_framework.authtoken.models import Token
from django.conf import settings

connect('opsclick-api-deploy',
        host='mongo',
        port=27017)

class User(Document):
    username = StringField(max_length=20)
    password = StringField(max_length=20)
    token = StringField(max_length=128)

#@receiver(post_save, sender=User)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)
