from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import User, Setup
from dopy.manager import DoManager
from abc import ABCMeta, abstractmethod
import boto3
from botocore.exceptions import NoRegionError


class Cloud(metaclass=ABCMeta):
    def __init__(self, credentials):
        self.access_key, self.secret_key = credentials

    @abstractmethod
    def get_session(self):
        pass
    @abstractmethod
    def get_cloud_info(self):
        pass


class DigitalOcean(Cloud):

    def __init__(self, credentials):
        super().__init__(credentials)
        self.name = 'DigitalOcean'
        self.do_session = DoManager(None, self.access_key, api_version=2)

    def get_session(self):
        pass

    def get_cloud_info(self, params):
        vals = {
            'images': self.get_distribution_images(params),
            'regions': self.get_regions(),
            'sizes': self.get_sizes()
        }
        return vals

    def get_distribution_images(self, params):
        data = self.do_session.all_images(params)
        if data:
            return data
        return False

    def get_regions(self):
        regions = self.do_session.all_regions()
        if regions:
            return regions
        return False

    def get_sizes(self):
        sizes = self.do_session.sizes()
        if sizes:
            return sizes
        return False


class AWS(Cloud):

    def __init__(self, credentials):
        super().__init__(credentials)
        self.name = 'AWS'
        self.aws_session = boto3.session.Session(
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )

    def get_session(self):
        pass

    def get_cloud_info(self, params):
        vals = {
            'images': self.get_images(),
            'regions': self.get_regions(),
            'types': self.get_instance_types('us-west-1')
        }
        return vals

    def get_images(self):
        data = ['image1', 'image2']
        return data

    def get_instance_types(self, region):
        try:
            ec2 = self.aws_session.resource('ec2', region_name=region)
        except NoRegionError as err:
            raise

        data = ec2.meta.client.describe_images()
        return data

    def get_regions(self):
        data = self.aws_session.get_available_regions('ec2', partition_name='aws')
        return data
