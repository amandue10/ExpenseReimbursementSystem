from abc import ABC, abstractmethod

from entities.manager import Manager


class ManagerDAO(ABC):
    # get all manager credentials
    @abstractmethod
    def get_manager_by_credentials(self, manager_id: int, first_name: str, last_name: str, password: str):
        pass
