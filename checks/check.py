from abc import ABC, abstractmethod

from enum import Enum


class Severity(Enum):
    HIGH = 'high',
    MEDIUM = 'medium',
    LOW = 'low'


class Cloud(Enum):
    AWS = 'aws',
    GOOGLE = 'google',


class Check(ABC):
    def __init__(self, client):
        self.client = client

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
