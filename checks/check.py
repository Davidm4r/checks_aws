from abc import ABC, abstractmethod

from enum import Enum


class Severity(Enum):
    HIGH = 'high',
    MEDIUM = 'medium',
    LOW = 'low'


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
