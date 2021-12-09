from abc import ABC, abstractmethod

from entities.reimbursement_request import ReimbursementRequest


class ReimbursementRequestDAO(ABC):

    # employee create reimbursement request
    @abstractmethod
    def create_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        pass

    # get reimbursement requests by employee id
    @abstractmethod
    def get_reimbursement_requests_by_id(self, employee_id: int) -> ReimbursementRequest:
        pass
