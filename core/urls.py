from django.conf.urls import include, url

from . import views
from . import digitalocean
from . import aws

service_patterns = ([
    url(r'^$', views.service_list, name='service_list'),
    url(r'^(?P<service_name>[\w-]+)$', views.service_detail, name='service_detail')
], 'service')

setup_patterns = ([
    url(r'^$', views.setup_service, name='setup_service'),
], 'setup')

digitalocean_patterns = ([
    url(r'^images$', digitalocean.distribution_images, name='digitalocean images list'),
    url(r'^regions$', digitalocean.regions, name='digitalocean regions list'),
    url(r'^sizes$', digitalocean.sizes, name='digitalocean sizes list'),
], 'digitalocean')

aws_patterns = ([
    url(r'^instance_types$', aws.instance_types, name='aws instance types list'),
    url(r'^regions$', aws.regions, name='aws regions list'),
], 'aws')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^service/', include(service_patterns)),
    url(r'^setup', include(setup_patterns)),
    url(r'^digitalocean/', include(digitalocean_patterns)),
    url(r'^aws/', include(aws_patterns)),
    url(r'^test_serializer', views.test_serializer, name='endpoint to test serializers'),
]
