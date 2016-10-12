from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def get_aws_manager(access_key, secret_key):
    pass

@api_view(['GET'])
def distribution_images(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
