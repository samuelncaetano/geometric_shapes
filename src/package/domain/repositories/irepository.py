from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def list_all(self):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def remove(self, index):
        pass
