from api.settings import BASE_DIR
from .models import Service, Cloud
import logging
import os

_logger = logging.getLogger(__name__)

class Services():

    def __init__(self):
        self.service_dir = "{0}/services".format(BASE_DIR)

    def load(self):
        _logger.info("Loading Services")


class Clouds():

    def __init__(self):
        self.cloud_dir = "{0}/clouds".format(BASE_DIR)

    def load(self):
        for dirname, dirnames, filenames in os.walk(self.cloud_dir):
            if 'lib' in dirnames:
                dirnames.remove('lib')

            # print path to all subdirectories first.
            # for subdirname in dirnames:
            #     print(os.path.join(dirname, subdirname))
            print(filenames)
            # print path to all filenames.
            # for filename in filenames:
            #     print(os.path.join(dirname, filename))
        _logger.info("Loading Clouds")

services = Services()
clouds = Clouds()

services.load()
clouds.load()
