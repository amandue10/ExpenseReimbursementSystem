from data_access_layer.implementation_classes.employee_postgres_dao import EmployeePostgresDAO
from service_layer.implementation_services.employee_postgres_service import EmployeePostgresService

employee_dao = EmployeePostgresDAO()
employee_service = EmployeePostgresService(employee_dao)

employee_id = 1
password = "password"
first_name = "Henry"
last_name = "Cantu"


def test_validate_correct_credentials():
    validation = employee_service.service_validate_employee_login(employee_id, first_name, last_name, password)
    assert validation
