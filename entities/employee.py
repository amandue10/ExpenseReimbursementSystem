class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, password: str):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def make_manager_dictionary(self):
        return {
            "employeeId": self.employee_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "password": self.password
        }

    def __str__(self):
        return "employee id: {}, first name: {}, last name: {}, password: {}".format(self.employee_id, self.first_name,
                                                                                     self.last_name, self.password)
