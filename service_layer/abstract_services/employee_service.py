from abc import ABC, abstractmethod

from entities.employee import Employee
from entities.reimbursement_request import ReimbursementRequest


class EmployeeService(ABC):

    # employee login
    @abstractmethod
    def service_validate_employee_login(self, employee_id: int, first_name: str, last_name: str, password: str):
        pass

    # Employee create RR and get all rr by employee id are
    # being handled by
    # reimbursement request service.
