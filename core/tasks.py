from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import shared_task
from subprocess import call, run, PIPE, Popen
from api.settings import BASE_DIR
from rest_framework.renderers import JSONRenderer
import os
import json


logger = get_task_logger(__name__)
env = os.environ

@shared_task
def ansible_setup(data=None):
    if not data:
        return
    (service, cloud, options) = data['service'], data['cloud'], data['options']

    cloud_path = "{0}/clouds/{1}".format(BASE_DIR, cloud)
    cloud_playbook = cloud_path + "/main.yml"
    cloud_host = cloud_path + "/hosts"
    logger.debug("%s" % options)

    if service and cloud:
        logger.debug("configuring the cloud %s" % (cloud))
        command = ['ansible-playbook', cloud_playbook, '-i', cloud_host, '--extra-vars', str(options)]
        logger.debug(" ".join(command))

        env['ANSIBLE_CONFIG'] = cloud_path + "/ansible.cfg"
        ansible_call = Popen(command, stdout=PIPE, env=env)
        try:
            output, errs = ansible_call.communicate()
        except:
            ansible_call.kill()
            output, errs = ansible_call.communicate()
        outs  = json.loads(output.decode("utf-8"))

        if options['state'] in ("present"):
            for task in outs['tasks']:
                info_host = task['hosts']['localhost']
                if info_host:
                    logger.info(info_host['results'][0]['droplets']['networks']['v4'][0]['ip_address'])

            hosts = ""
#            installing_docker(hosts)

    else:
        logger.warn("We need to know the service and the cloud")

@shared_task
def installing_docker(hosts=None):
    if not hosts:
        logger.info("You need to define the hosts")
        return

    docker_path = "{0}/clouds/lib/{1}".format(BASE_DIR, "docker")
    docker_playbook = docker_path + "/main.yml"

    env['ANSIBLE_CONFIG'] = cloud_path + "/ansible.cfg"
    command = ['ansible-playbook', docker_playbook, '-i', hosts_file]
    ansible_call = Popen(command, stdout=PIPE, env=env)
    try:
        output, errs = ansible_call.communicate()
    except:
        ansible_call.kill()
        output, errs = ansible_call.communicate()

