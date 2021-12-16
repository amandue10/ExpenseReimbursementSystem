from data_access_layer.implementation_classes.manager_postgres_dao import ManagerPostgresDAO

manager_dao = ManagerPostgresDAO()
manager_id = 1
password = "password"
first_name = "Amanda"
last_name = "Jones"


def test_select_all_emp_information_by_employee_id():
    validation = manager_dao.get_manager_by_credentials(manager_id, first_name, last_name, password)
    assert validation[0] == 1
