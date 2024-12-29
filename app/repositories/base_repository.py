from abc import ABC, abstractmethod


class IRepository(ABC):

    @abstractmethod
    def get(self, entity_id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def update(self, entity_id: int, entity):
        pass

    @abstractmethod
    def delete(self, entity_id: int):
        pass
