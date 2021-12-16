from data_access_layer.abstract_classes.manager_dao import ManagerDAO
from entities.manager import Manager
from util.database_connection import connection


class ManagerPostgresDAO(ManagerDAO):
    # green pytest
    # get all manager information for login
    def get_manager_by_credentials(self, manager_id: int, first_name: str, last_name: str, password: str):
        sql = "select manager_id from project1.manager where manager_id = %s and first_name = %s and last_name = " \
              "%s and password = %s "
        cursor = connection.cursor()
        cursor.execute(sql, (manager_id, first_name, last_name, password))
        validated = cursor.fetchone()
        return validated
