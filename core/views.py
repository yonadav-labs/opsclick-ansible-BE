from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
    user = User(username="luis", password="123")
    user.save()
    num = User.objects().count()

    return HttpResponse('it works! %d' % num)
