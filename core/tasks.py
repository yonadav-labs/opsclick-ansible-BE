from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import shared_task, task, chain
from subprocess import call, run, PIPE, Popen
from api.settings import BASE_DIR
from rest_framework.renderers import JSONRenderer
import os
import json
from .serializers import SetupSerializer, AnsiblePlaybookSerializer
from .models import Setup, AnsiblePlaybook
from tempfile import NamedTemporaryFile

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
        pb_serializer = AnsiblePlaybookSerializer(data=outs)

        if pb_serializer.is_valid():
            pb_instance = pb_serializer.save()
            data['playbook'] = pb_instance.id

            setup = Setup(service=service,
                          cloud=cloud,
                          options=options,
                          playbook=data['playbook'])
            setup.save()

            code = """
        function() {
            var droplets_ip = []
            db[collection].find(query).forEach(function(doc) {
                doc.plays.forEach(function(play) {
                    play.tasks.forEach(function(task) {
                        if(task.hosts.localhost.results) {
                            task.hosts.localhost.results.forEach(function(result) {
                                if(result.droplet) {
                                    droplets_ip.push(result.droplet.ip_address);
                                }
                            });
                        }
                    });
                });
            });
            if(droplets_ip.length > 0){
                return droplets_ip;
            } 
            return false;
        }
        """
        return AnsiblePlaybook.objects.filter(id=pb_instance.id,).exec_js(code)
#            logger.info(AnsiblePlaybook.objects.filter(id=pb_instance.id,).exec_js(code))
    else:
        logger.warn("We need to know the service and the cloud")


@shared_task
def install_docker(hosts=None):
    if not hosts:
        logger.info("You need to define the hosts")
        return

    docker_path = "{0}/clouds/lib/{1}".format(BASE_DIR, "docker")
    docker_playbook = docker_path + "/main.yml"
    hosts_template = """

    """

    env['ANSIBLE_CONFIG'] = docker_path + "/ansible.cfg"
#    command = ['ansible-playbook', docker_playbook, '-i', ]
#    logger.info("###--- JUST TESTING ---###")
    # ansible_call = Popen(command, stdout=PIPE, env=env)
    # try:
    #     output, errs = ansible_call.communicate()
    # except:
    #     ansible_call.kill()
    #     output, errs = ansible_call.communicate()

