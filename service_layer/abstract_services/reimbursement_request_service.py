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

    # Get pending reimbursement requests
    @abstractmethod
    def service_get_pending_reimbursement_requests(self) -> list[ReimbursementRequest]:
        pass

    # Get completed reimbursement requests
    @abstractmethod
    def service_get_completed_reimbursement_requests(self) -> list[ReimbursementRequest]:
        pass

    # update for manager to determine, approval, denial, and comment.
    # pytest green and persisting to database
    @abstractmethod
    def service_update_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        pass
