from data_access_layer.abstract_classes.reimbursement_request_dao import ReimbursementRequestDAO
from entities.reimbursement_request import ReimbursementRequest
from util.database_connection import connection


class ReimbursementRequestPostgresDAO(ReimbursementRequestDAO):
    # create request is green in pycharm, persisting to database
    def create_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        sql = "insert into project1.reimbursement_request values(default, %s, %s, %s, %s, %s, %s) returning " \
              "request_id"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement_request.employee_id, reimbursement_request.manager_id,
                             reimbursement_request.request_amount, reimbursement_request.request_comment,
                             reimbursement_request.request_comment2, reimbursement_request.request_status))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        reimbursement_request.request_id = generated_id
        return reimbursement_request

    # get all reimbursement info by employee id
    # pytest is green.
    def get_reimbursement_requests_by_id(self, employee_id: int) -> ReimbursementRequest:
        sql = "select * from project1.reimbursement_request where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        request_record = cursor.fetchone()
        request = ReimbursementRequest(*request_record)
        return request

    # pytest is green
    # get all reimbursement history
    def get_all_reimbursement_history(self) -> list[ReimbursementRequest]:
        sql = "select * from project1.reimbursement_request"
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(ReimbursementRequest(*reimbursement))
        return reimbursement_list

    def update_reimbursement_request(self, employee_id: int) -> ReimbursementRequest:
        pass

