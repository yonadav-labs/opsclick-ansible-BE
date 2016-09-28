from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import shared_task
from subprocess import call
from api.settings import BASE_DIR
from rest_framework.renderers import JSONRenderer


logger = get_task_logger(__name__)

@shared_task
def ansible_setup(data=None):
    if not data:
        return
    (service, cloud, options) = data['service'], data['cloud'], data['options']

    cloud_path = "{0}/clouds/{1}".format(BASE_DIR, cloud)
    cloud_playbook = cloud_path + "/main.yml"
    cloud_host = cloud_path + "/hosts"
    logger.info("%s" % options)

    if service and cloud:
        logger.info("configuring the cloud %s" % (cloud))
        command = ['ansible-playbook', cloud_playbook, '-i', cloud_host, '--extra-vars', str(options)]
        logger.info(" ".join(command))
        call(command)

        logger.info("setting up %s in %s" % (service,cloud))
        command = ['ansible-playbook', cloud_playbook, '-i', cloud_host]
        logger.info(" ".join(command))
#        call(command)
    else:
        logger.warn("We need to know the service and the cloud")
