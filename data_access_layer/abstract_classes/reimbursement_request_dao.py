from abc import ABC, abstractmethod

from entities.reimbursement_request import ReimbursementRequest


class ReimbursementRequestDAO(ABC):

    # create reimbursement request
    @abstractmethod
    def create_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        pass

    # get all reimbursement requests by employee id
    @abstractmethod
    def get_reimbursement_requests_by_id(self, employee_id: int) -> list[ReimbursementRequest]:
        pass

    # get all reimbursements information List
    @abstractmethod
    def get_all_reimbursement_history(self) -> list[ReimbursementRequest]:
        pass

    # update reimbursement request
    @abstractmethod
    def update_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        pass
