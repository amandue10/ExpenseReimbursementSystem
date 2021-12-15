from data_access_layer.abstract_classes.employee_dao import EmployeeDAO
from entities.employee import Employee
from util.database_connection import connection


class EmployeePostgresDAO(EmployeeDAO):
    # green pytest
    # get all employe information for login
    def get_employee_information_by_id(self, employee_id: int) -> Employee:
        sql = "select * from project1.employee where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        employee_record = cursor.fetchone()
        employee = Employee(*employee_record)
        return employee
