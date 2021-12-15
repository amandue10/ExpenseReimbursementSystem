from abc import ABC, abstractmethod

from entities.manager import Manager


class ManagerDAO(ABC):
    # get all manager information by manager id
    @abstractmethod
    def get_manager_information_by_id(self, manager_id: int) -> Manager:
        pass
