from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import User, Service, Setup
from core.serializers import ServiceSerializer, UserSerializer, SetupSerializer
from core.tasks import ansible_setup
from django.contrib.auth import authenticate
from django_mongoengine.mongo_auth.models import MongoUser

@api_view(['GET', 'POST'])
def index(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def service_list(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def service_detail(request, service_name):
    try:
        service = Service.objects.get(name=service_name)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    if request.method == 'PUT':
        pass

    if request.method == 'DELETE':
        pass

@api_view(['POST'])
def setup_service(request):
    if request.method == 'POST':
        serializer = SetupSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer.data)
            ansible_setup.delay(serializer.data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)

