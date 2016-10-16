from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import boto3

def get_aws_session(access_key, secret_key):
    return boto3.session.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

@api_view(['GET'])
def images(request):
    if request.method == 'GET':
        access_key = request.META.get('HTTP_ACCESS_KEY')
        secret_key = request.META.get('HTTP_SECRET_KEY')

        data = ""

        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def instance_types(request):
    if request.method == 'GET':
        access_key = request.META.get('HTTP_ACCESS_KEY')
        secret_key = request.META.get('HTTP_SECRET_KEY')
        region = request.get('region')

        aws_session = get_aws_session(access_key, secret_key)
        ec2 = aws_session.resource('ec2', region_name=region)
        data = ec2.describe_images()

        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def regions(request):
    if request.method == 'GET':
        access_key = request.META.get('HTTP_ACCESS_KEY')
        secret_key = request.META.get('HTTP_SECRET_KEY')

        aws_session = get_aws_session(access_key, secret_key)
        data = aws_session.get_available_regions('ec2', partition_name='aws')

        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
