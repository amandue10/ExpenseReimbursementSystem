from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeDAO(ABC):
    # get all employee information by employee id
    @abstractmethod
    def get_employee_by_credentials(self, employee_id: int, password: str):
        pass
