from django.conf.urls import include, url

from . import views

service_patterns = ([
    url(r'^$', views.service_list, name='service_list'),
    url(r'^/(?P<service_name>[\w-]+)$', views.service_fields, name='service_detail'),
], 'service')

setup_patterns = ([
    url(r'^$', views.setup_service, name='setup_service'),
    url(r'^/status$', views.task_status, name='task_status')
], 'setup')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^service', include(service_patterns)),
    url(r'^cloud/(?P<cloud_name>[\w]+)$', views.cloud_detail, name='cloud fields'),
    url(r'^clouds$', views.clouds_info, name='cloud information'),
    url(r'^cloud/(?P<cloud_name>[\w]+)/assets$', views.get_assets, name='cloud assets information'),
    url(r'^setup', include(setup_patterns)),
    url(r'^test_serializer', views.test_serializer, name='endpoint to test serializers'),
    url(r'^jobs$', views.get_jobs, name='get jobs'),
]
