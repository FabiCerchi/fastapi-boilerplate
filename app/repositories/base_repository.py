"""
Base Repository Interface to define the CRUD methods that should be implemented by the repository classes
"""
from abc import ABC, abstractmethod


class IRepository(ABC):
    """
    Base Repository Interface to define the CRUD methods that should be implemented by the repository classes
    """
    @abstractmethod
    def get(self, entity_id: int):
        """
        Method to get an entity by id
        :param entity_id:
        :return:
        """
        pass

    @abstractmethod
    def get_all(self):
        """
        Method to get all entities
        :return: List[Entity]
        """
        pass

    @abstractmethod
    def add(self, entity):
        """
        Method to add a new entity
        :param entity:
        :return:
        """
        pass

    @abstractmethod
    def update(self, entity_id: int, entity):
        """
        Method to update an entity
        :param entity_id:
        :param entity:
        :return:
        """
        pass

    @abstractmethod
    def delete(self, entity_id: int):
        """
        Method to delete an entity
        :param entity_id:
        :return:
        """
        pass
