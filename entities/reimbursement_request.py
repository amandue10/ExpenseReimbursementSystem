
class ReimbursementRequest:
    def __init__(self, request_id: int, employee_id: int, manager_id: int, request_amount: int, request_comment: str,
                 request_comment2: str, request_status: str, rr_date):
        self.request_id = request_id
        self.employee_id = employee_id
        self.manager_id = manager_id
        self.request_amount = request_amount
        self.request_comment = request_comment
        self.request_comment2 = request_comment2
        self.request_status = request_status
        self.rr_date = rr_date

    def make_rr_dictionary(self):
        return {
            "requestId": self.request_id,
            "employeeId": self.employee_id,
            "managerId": self.manager_id,
            "requestAmount": self.request_amount,
            "requestComment": self.request_comment,
            "requestComment2": self.request_comment2,
            "requestStatus": self.request_status,
            "rrDate": self.rr_date

        }

    def __str__(self):
        return "request id: {}, employee id: {}, manager id: {}, request amount: {}, request comment: {}, " \
               "request comment2: {}," \
               " request status: {}, request date: {}".format(self.request_id, self.employee_id, self.manager_id,
                                                              self.request_amount, self.request_comment,
                                                              self.request_comment2,
                                                              self.request_status, self.rr_date)
