from abc import ABC, abstractmethod

from entities.manager import Manager


class ManagerService(ABC):

    # manager login
    @abstractmethod
    def service_validate_manager_login(self, manager_id: int, first_name: str, last_name: str, password: str):
        pass

    # reimbursement requests for managers to review
    # are being handled by
    # reimbursement request service.
