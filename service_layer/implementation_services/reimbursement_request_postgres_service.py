from data_access_layer.implementation_classes.reimbursement_request_postgres_dao import ReimbursementRequestPostgresDAO
from entities.reimbursement_request import ReimbursementRequest
from service_layer.abstract_services.reimbursement_request_service import ReimbursementRequestService


class ReimbursementRequestPostgresService(ReimbursementRequestService):

    def __init__(self, reimbursement_request_dao: ReimbursementRequestPostgresDAO):
        self.reimbursement_request_dao = reimbursement_request_dao

    def service_create_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        created_rr = self.reimbursement_request_dao.create_reimbursement_request(reimbursement_request)
        return created_rr

    def service_get_reimbursement_requests_by_id(self, employee_id: int) -> list[ReimbursementRequest]:
        return self.reimbursement_request_dao.get_reimbursement_requests_by_id(employee_id)

    def service_get_pending_reimbursement_requests(self) -> list[ReimbursementRequest]:
        return self.reimbursement_request_dao.get_pending_reimbursement_requests()

    def service_get_completed_reimbursement_requests(self) -> list[ReimbursementRequest]:
        return self.reimbursement_request_dao.get_completed_reimbursement_requests()

    def service_update_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        return self.reimbursement_request_dao.update_reimbursement_request(reimbursement_request)


