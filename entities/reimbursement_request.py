class ReimbursementRequest:
    def __init__(self, request_id: int, employee_id: int, request_amount: int, request_comment: str, request_status: bool):
        self.request_id = request_id
        self.employee_id = employee_id
        self.request_amount = request_amount
        self.request_comment = request_comment
        self.request_status = request_status

    def make_customer_dictionary(self):
        return {
            "requestId": self.request_id,
            "employeeId": self.employee_id,
            "requestAmount": self.request_amount,
            "requestComment": self.request_comment,
            "requestStatus": self.request_status,

        }

    def __str__(self):
        return "request id: {}, employee id: {}, request amount: {}, request comment: {}," \
               " request status: {}".format(self.request_id, self.employee_id,
                                            self.request_amount, self.request_comment, self.request_status)