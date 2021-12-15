from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeDAO(ABC):
    # get all employee information by employee id
    @abstractmethod
    def get_employee_information_by_id(self, employee_id: int) -> Employee:
        pass
