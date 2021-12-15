from data_access_layer.implementation_classes.employee_postgres_dao import EmployeePostgresDAO
from entities.employee import Employee
from entities.reimbursement_request import ReimbursementRequest
from service_layer.abstract_services.employee_service import EmployeeService


class EmployeePostgresService(EmployeeService):
    def __init(self, employee_dao: EmployeePostgresDAO):
        self.employee_dao = employee_dao

    def service_employee_login(self, employee_id: int) -> Employee:
        pass

    def service_employee_log_out(self, employee_id: int) -> Employee:
        pass
