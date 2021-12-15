from data_access_layer.implementation_classes.employee_postgres_dao import EmployeePostgresDAO

employee_dao = EmployeePostgresDAO()


def test_select_all_emp_information_by_employee_id():
    employee = employee_dao.get_reimbursement_requests_by_id(4)
    assert employee.employee_id == 4