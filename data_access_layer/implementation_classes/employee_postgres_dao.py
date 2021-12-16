from data_access_layer.abstract_classes.employee_dao import EmployeeDAO
from entities.employee import Employee
from util.database_connection import connection


class EmployeePostgresDAO(EmployeeDAO):
    # green pytest
    # get all employee information for login
    def get_employee_by_credentials(self, employee_id: int, password: str):
        sql = "select employee_id from project1.employee where employee_id = %s and password = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (employee_id, password))
        validated = cursor.fetchone()
        return validated
