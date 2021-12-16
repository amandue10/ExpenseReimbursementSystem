from data_access_layer.implementation_classes.manager_postgres_dao import ManagerPostgresDAO
from entities.manager import Manager
from service_layer.abstract_services.manager_service import ManagerService


class ManagerPostgresService(ManagerService):
    def __init__(self, manager_dao: ManagerPostgresDAO):
        self.manager_dao = manager_dao

    def service_validate_manager_login(self, manager_id: int, first_name: str, last_name: str, password: str):
        validation = self.manager_dao.get_manager_by_credentials(manager_id, first_name, last_name, password)
        if type(validation) == tuple:
            return True
        else:
            return False

