from django.apps import AppConfig
import os
from api.settings import BASE_DIR
import logging
from .models import Addon
from .serializers import AddonSerializer
from mongoengine.errors import ValidationError

_logger = logging.getLogger(__name__)

MANIFEST = '__opsclick__.py'
addons_paths = []

class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        Addon.drop_collection()
        self.load_modules()

    def initialize_paths(self):
        global addons_paths

        for mod_type in ['clouds', 'services']:
            base_path = os.path.abspath(os.path.join(BASE_DIR, mod_type))

            for path, dirnames, filenames in os.walk(base_path):
                if os.path.exists(os.path.join(path, MANIFEST)):
                    addons_paths.append(path)

    def register_module(self, info):
        addon = Addon.objects(name__exact=info['name'],
                              type__exact=info['type'],
                              version__exact=info['version'])
        if not addon:
            serializer = AddonSerializer(data=info)

            if serializer.is_valid():
                serializer.save()

    def load_modules(self):
        self.initialize_paths()

        for adp in addons_paths:
            ops_file = adp and os.path.join(adp, MANIFEST) or False
            if ops_file:
                info = {}
                if os.path.isfile(ops_file):
                    # default values for descriptor
                    info = {
                        'name': '',
                        'type': '',
                        'author': 'OpsClick',
                        'category': 'Uncategorized',
                        'version': '1.0',
                    }
                    # info.update(zip(
                    #     'depends'.split(),
                    #     iter(list, None)))

                    f = open(ops_file)
                    try:
                        info.update(eval(f.read()))
                    except Exception:
                        _logger.info('Error when trying to fetch informations for '
                                     'module %s', adp)
                    finally:
                        f.close()

                    self.register_module(info)

