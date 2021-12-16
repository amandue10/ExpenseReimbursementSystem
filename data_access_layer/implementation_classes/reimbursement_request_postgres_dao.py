from data_access_layer.abstract_classes.reimbursement_request_dao import ReimbursementRequestDAO
from entities.reimbursement_request import ReimbursementRequest
from util.database_connection import connection


class ReimbursementRequestPostgresDAO(ReimbursementRequestDAO):
    # create request is green in pycharm, persisting to database
    def create_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        sql = "insert into project1.reimbursement_request values(default, %s, %s, %s, %s, %s, %s, %s) returning " \
              "request_id"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement_request.employee_id, reimbursement_request.manager_id,
                             reimbursement_request.request_amount, reimbursement_request.request_comment,
                             reimbursement_request.request_comment2, reimbursement_request.request_status,
                             reimbursement_request.rr_date))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        reimbursement_request.request_id = generated_id
        return reimbursement_request

    # pytest is green.
    # Get all reimbursement requests by employee_id
    def get_reimbursement_requests_by_id(self, employee_id: int) -> list[ReimbursementRequest]:
        sql = "select * from project1.reimbursement_request where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        request_record = cursor.fetchall()
        request_list = []
        for reimbursement_request in request_record:
            request_list.append(ReimbursementRequest(*reimbursement_request))
        return request_list

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

    # update for manager to determine, approval, denial, and comment.
    # pytest green and persisting to database
    def update_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        sql = "update project1.reimbursement_request set employee_id = %s, manager_id = %s, request_amount = %s, " \
              "request_comment1 = %s, request_comment2 = %s, request_status = %s, rr_date = %s where request_id = %s "
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement_request.employee_id, reimbursement_request.manager_id,
                             reimbursement_request.request_amount, reimbursement_request.request_comment,
                             reimbursement_request.request_comment2, reimbursement_request.request_status,
                             reimbursement_request.rr_date, reimbursement_request.request_id))
        connection.commit()
        return reimbursement_request

    # pytest green
    # get pending reimbursement requests
    def get_pending_reimbursement_requests(self) -> list[ReimbursementRequest]:
        sql = "select * from project1.reimbursement_request where request_status like '% %' "
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(ReimbursementRequest(*reimbursement))
        return reimbursement_list

    # pytest green
    # get completed reimbursement requests
    def get_completed_reimbursement_requests(self) -> list[ReimbursementRequest]:
        sql = "select * from project1.reimbursement_request where request_status like '%completed%'"
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursements in reimbursement_records:
            reimbursement_list.append(ReimbursementRequest(*reimbursements))
        return reimbursement_list
