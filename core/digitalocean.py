from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import User, Service, Setup
from core.serializers import OptionsSerializer
#from core.tasks import digitalocean_api
from dopy.manager import DoManager

def get_do_manager(access_key):
    return DoManager(None, access_key, api_version=2)

@api_view(['GET'])
def distribution_images(request):
    if request.method == 'GET':
        access_key = request.META.get('HTTP_ACCESS_KEY')

        if access_key:
            do = get_do_manager(access_key)
            return Response(do.all_images(request.query_params), status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def regions(request):
  if request.method == 'GET':
        access_key = request.META.get('HTTP_ACCESS_KEY')

        if access_key:
            do = get_do_manager(access_key)
            regions = do.all_regions()
            if regions:
                return Response(regions, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_504_GATEWAY_TIMEOUT)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def sizes(request):
  if request.method == 'GET':
        access_key = request.META.get('HTTP_ACCESS_KEY')

        if access_key:
            do = get_do_manager(access_key)
            sizes = do.sizes()
            if sizes:
                return Response(sizes, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_504_GATEWAY_TIMEOUT)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

