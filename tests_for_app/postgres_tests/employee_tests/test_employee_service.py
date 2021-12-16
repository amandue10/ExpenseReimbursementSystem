from data_access_layer.implementation_classes.employee_postgres_dao import EmployeePostgresDAO
from service_layer.implementation_services.employee_postgres_service import EmployeePostgresService

employee_dao = EmployeePostgresDAO()
employee_service = EmployeePostgresService(employee_dao)

employee_id = 4
password = "password"


def test_validate_correct_credentials():
    validation = employee_service.service_validate_employee_login(employee_id, password)
    assert validation
