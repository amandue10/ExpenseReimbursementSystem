from data_access_layer.implementation_classes.employee_postgres_dao import EmployeePostgresDAO
from service_layer.abstract_services.employee_service import EmployeeService


class EmployeePostgresService(EmployeeService):
    def __init__(self, employee_dao: EmployeePostgresDAO):
        self.employee_dao = employee_dao

    def service_validate_employee_login(self, employee_id: int, first_name: str, last_name: str, password: str):
        validation = self.employee_dao.get_employee_by_credentials(employee_id, first_name, last_name, password)
        if type(validation) == tuple:
            return True
        else:
            return False