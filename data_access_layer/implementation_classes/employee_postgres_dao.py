from data_access_layer.abstract_classes.employee_dao import EmployeeDAO
from entities import employee
from entities.employee import Employee
from util.database_connection import connection


class EmployeePostgresDAO(EmployeeDAO):
    # green pytest
    # get all employee information for login
    def get_employee_by_credentials(self, employee_id: int, first_name: str, last_name: str, password: str):
        sql = "select employee_id from project1.employee where employee_id = %s and first_name = %s and last_name = " \
              "%s and password = %s "
        cursor = connection.cursor()
        cursor.execute(sql, (employee_id, first_name, last_name, password))
        validated = cursor.fetchone()
        return validated
