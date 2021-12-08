class Manager:
    def __init__(self, manager_id: int, first_name: str, last_name: str):
        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name

    def make_manager_dictionary(self):
        return {
            "managerId": self.manager_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
        }

    def __str__(self):
        return "manager id: {}, first name: {}, last name: {}".format(self.manager_id, self.first_name,
                                                                      self.last_name)
