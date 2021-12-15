from abc import ABC, abstractmethod

from entities.employee import Employee
from entities.reimbursement_request import ReimbursementRequest


class EmployeeService(ABC):

    # employee login
    @abstractmethod
    def service_employee_login(self, employee_id: int) -> Employee:
        pass

    # employee log out
    @abstractmethod
    def service_employee_log_out(self, employee_id: int) -> Employee:
        pass

    # Employee create RR and get all rr by employee id are
    # being handled by
    # reimbursement request service.
