from abc import ABC, abstractmethod

from entities.manager import Manager


class ManagerService(ABC):

    # manager login
    @abstractmethod
    def service_manager_login(self, manager_id: int) -> Manager:
        pass

    # manager log out
    @abstractmethod
    def service_manager_log_out(self, manager_id: int) -> Manager:
        pass

    # reimbursement requests for managers to review
    # are being handled by
    # reimbursement request service.
