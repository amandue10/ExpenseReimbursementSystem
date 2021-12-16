from data_access_layer.implementation_classes.manager_postgres_dao import ManagerPostgresDAO
from entities.manager import Manager
from service_layer.abstract_services.manager_service import ManagerService


class ManagerPostgresService(ManagerService):
    def __init(self, manager_dao: ManagerPostgresDAO):
        self.manager_dao = manager_dao

    def service_manager_login(self, manager_id: int) -> Manager:
        pass

    def service_manager_log_out(self, manager_id: int) -> Manager:
        pass
