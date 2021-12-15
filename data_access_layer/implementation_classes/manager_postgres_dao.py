from data_access_layer.abstract_classes.manager_dao import ManagerDAO
from entities.manager import Manager
from util.database_connection import connection


class ManagerPostgresDAO(ManagerDAO):
    # green pytest
    # get all manager information for login
    def get_manager_information_by_id(self, manager_id: int) -> Manager:
        sql = "select * from project1.manager where manager_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        manager_record = cursor.fetchone()
        manager = Manager(*manager_record)
        return manager
