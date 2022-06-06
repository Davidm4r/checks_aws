from abc import ABC, abstractmethod
import boto3
from enum import Enum


class Severity(Enum):
    HIGH = 'high',
    MEDIUM = 'medium',
    LOW = 'low'


class Cloud(Enum):
    AWS = 'aws',
    GOOGLE = 'google',

class Client:
    def __init__(self, service, region_name=None):
        if region_name:
            self.client = boto3.client(service, region_name=region_name)
        else:
            self.client = boto3.client(service)


class Check(ABC):

    @property
    @abstractmethod
    def title(self):
        return "CheckXX"

    @property
    @abstractmethod
    def description(self):
        return "Description"


    @property
    @abstractmethod
    def severity(self):
        return Severity.LOW

    @abstractmethod
    def execute(self):
        pass
