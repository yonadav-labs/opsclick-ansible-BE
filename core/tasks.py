from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import shared_task
from subprocess import call

logger = get_task_logger(__name__)

@shared_task
def ansible_setup(service=None, cloud=None):
    if service and cloud:
        logger.info("setting up %s in %s" % (service,cloud))
    else:
        logger.warn("We need to know the service and the cloud")
