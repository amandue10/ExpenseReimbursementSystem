from data_access_layer.implementation_classes.employee_postgres_dao import EmployeePostgresDAO

employee_dao = EmployeePostgresDAO()
employee_id = 4
password = "password"


def test_select_all_emp_information_by_employee_id():
    validated = employee_dao.get_employee_by_credentials(employee_id, password)
    assert validated[0] == 4
