from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import User, Addon, Setup, AnsiblePlaybook
from core.serializers import AddonSerializer, SetupSerializer, AnsiblePlaybookSerializer
from core.tasks import running_setup
from django.contrib.auth import authenticate
from django_mongoengine.mongo_auth.models import MongoUser
import mongoengine
from . import clouds
import json

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def service_list(request):

    if request.method == 'GET':
        try:
            services = Addon.objects(type__exact='service')
        except Addon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AddonSerializer(services, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def service_fields(request, service_name):
    try:
        service = Addon.objects.get(name=service_name)
    except Addon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddonSerializer(service)
        return Response(serializer.data['fields'], status.HTTP_200_OK)


@api_view(['GET'])
def clouds_info(request):
    if request.method == 'GET':
        access_key = request.META.get('HTTP_ACCESS_KEY')
        secret_key = request.META.get('HTTP_SECRET_KEY')
        cloud_name = request.META.get('HTTP_CLOUD')
        try:
            cloud_class = getattr(clouds, cloud_name)
        except AttributeError as err:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        except TypeError as err:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        cloud = cloud_class((access_key, secret_key))
        try:
            data = cloud.get_cloud_info(request.query_params)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def cloud_detail(request, cloud_name):
    try:
        cloud = Addon.objects.get(name=cloud_name)
    except Addon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddonSerializer(cloud)
        return Response(serializer.data['fields'], status.HTTP_200_OK)

"""
@api {post} /setup Setup a cloud with Addon
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
		"ssh_pub_key": [{
			"name": "user",
			"key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMhY7Lp2uN5yH0qv9o6d3EuBmBm9xZ9STxFo/negDSOMV2p2zRdkw1JuUurVFVx+8JgWg25/kMKOJmR01Ri928CAoOsFzxV9qqPlRXuOsTqim6g4+YdLnwci5SsJ7Ek7XYAtZXvdXUV2R8xtHX9HUz3Wv1kfFYmRzz5VzSGk7OS5Ov5p03j6sggUjkrgJo2ho105jVaeYPLL7o17Y3e4gtx6aZo93DMEeXm17VCYS3Gy7Wrka4+e4LKHHQu8coIPS9WXuC+rwQjZJzujSj5FKWhujUagZvwHxr+Sh2uzJ86PZSZla3+o2KpZvoDIzZ85Sa4X4UTE2tb9WuYAKryhNd ansible-generated on xyklexwifi.oficina.ongen.com.ve"
			}],
		"access_key":"71b1ebc1e0c4a233c917276cf1f6bd5cd54dd3433c07bdcb9924cc98cd917886"
	}
    }

"""
@api_view(['POST'])
def setup_service(request):
    if request.method == 'POST':
        request.data['state'] = 'present'
        serializer = SetupSerializer(data=request.data)

        if serializer.is_valid():
            res = running_setup(serializer.data)

            return Response(res, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def task_status(request):
    if request.method == 'GET':
        task_id = request.META.get('HTTP_TASK_ID')
        if task_id:
            from celery.result import AsyncResult
            task = AsyncResult(str(task_id))
            return Response(task.state, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET'])
def get_assets(request):
    if request.method == 'GET':
        access_key = request.META.get('HTTP_ACCESS_KEY')
        secret_key = request.META.get('HTTP_SECRET_KEY')
        cloud_name = request.META.get('HTTP_CLOUD')

        try:
            cloud_class = getattr(clouds, cloud_name)
        except AttributeError as err:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        except TypeError as err:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        cloud = cloud_class((access_key, secret_key))
        try:
            data = cloud.get_assets()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_jobs(request):
    if request.method == 'GET':
        user = request.META.get('HTTP_USER')

        fields = [

        ]
        if user:
            queryset = Setup.objects.filter(user=user) \
                                    .only('id',
                                          'options.size',
                                          'options.image',
                                          'options.region',
                                          'options.service_opts',
                                          'playbook',
                                          'cloud',
                                          'service',
                                          'status')
            if len(queryset) > 0:
                docs = json.loads(queryset.to_json())
                for doc in docs:
                    try:
                        play = AnsiblePlaybook.objects.filter(id=doc['playbook']['$oid'])
                        #                                              .only('plays')

                        doc['playbook'] = json.loads(play.to_json())[0]
                    except:
                        pass
                return Response(docs, status=status.HTTP_200_OK)
            else:
                return Response("The user does not exists", status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_setup_status(request, setup_id):
    if request.method == 'GET':
        try:
            job = Setup.objects.get(id=setup_id)
            return Response(job.status, status.HTTP_200_OK)
        except mongoengine.errors.DoesNotExist:
            return Response("The job does not exist", status.HTTP_404_NOT_FOUND)


