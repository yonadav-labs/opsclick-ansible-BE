from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import User, Service, Setup
from core.serializers import ServiceSerializer, UserSerializer, SetupSerializer, AnsiblePlaybookSerializer
from core.tasks import running_setup
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


"""
@api {post} /setup Setup a cloud with Service
@apiName PostSetup
@apiGroup Core

@apiParam {String} service Name of the service.
@apiParam {String} cloud Name of the cloud.
@apiParam {Dict[]} options List of options for the cloud

@apiParamExample {json} Request-Example:
    {
	"service":"mysql",
	"cloud":"digitalocean",
	"options":{
		"droplets":["uno"],
		"state": "absent",
		"size": "512mb",
		"image": "ubuntu-14-04-x64",
		"region": "sgp1",
		"ssh_pub_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMhY7Lp2uN5yH0qv9o6d3EuBmBm9xZ9STxFo/negDSOMV2p2zRdkw1JuUurVFVx+8JgWg25/kMKOJmR01Ri928CAoOsFzxV9qqPlRXuOsTqim6g4+YdLnwci5SsJ7Ek7XYAtZXvdXUV2R8xtHX9HUz3Wv1kfFYmRzz5VzSGk7OS5Ov5p03j6sggUjkrgJo2ho105jVaeYPLL7o17Y3e4gtx6aZo93DMEeXm17VCYS3Gy7Wrka4+e4LKHHQu8coIPS9WXuC+rwQjZJzujSj5FKWhujUagZvwHxr+Sh2uzJ86PZSZla3+o2KpZvoDIzZ85Sa4X4UTE2tb9WuYAKryhNde",
		"access_key":"71b1ebc1e0c4a233c917276cf1f6bd5cd54dd3433c07bdcb9924cc98cd917886"
	}
    }

"""
@api_view(['POST'])
def setup_service(request):
    if request.method == 'POST':
        serializer = SetupSerializer(data=request.data)

        if serializer.is_valid():
            running_setup(serializer.data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def test_serializer(request):
    if request.method == 'POST':
        serializer = AnsiblePlaybookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
