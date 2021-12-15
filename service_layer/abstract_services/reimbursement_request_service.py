from abc import ABC, abstractmethod

from entities.reimbursement_request import ReimbursementRequest


class ReimbursementRequestService(ABC):

    # employee create rr request
    @abstractmethod
    def service_create_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        pass

    # get all reimbursement requests by employee id
    @abstractmethod
    def service_get_reimbursement_requests_by_id(self, employee_id: int) -> ReimbursementRequest:
        pass
