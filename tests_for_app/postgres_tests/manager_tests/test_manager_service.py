from data_access_layer.implementation_classes.manager_postgres_dao import ManagerPostgresDAO
from service_layer.implementation_services.manager_postgres_service import ManagerPostgresService

manager_dao = ManagerPostgresDAO()
manager_service = ManagerPostgresService(manager_dao)

manager_id = 1
password = "password"
first_name = "Amanda"
last_name = "Jones"


def test_validate_correct_credentials():
    validation = manager_service.service_validate_manager_login(manager_id, first_name, last_name, password)
    assert validation
