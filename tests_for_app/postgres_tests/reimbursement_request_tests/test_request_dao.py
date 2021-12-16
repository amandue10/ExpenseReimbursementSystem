from data_access_layer.implementation_classes.reimbursement_request_postgres_dao import ReimbursementRequestPostgresDAO
from entities.reimbursement_request import ReimbursementRequest

request_dao = ReimbursementRequestPostgresDAO()

new_request = ReimbursementRequest(1, 3, 1, 200, "ice machine", " ", " ", '05 Dec 2012')

status = {"approval-completed"}
status.add("denied-completed")
# status.add("approval- with comment")
# status.add("denied- with comment")

random_status = status.pop()

update_rr = ReimbursementRequest(2, 3, 1, 300, "birthday party", "I made this decision ...", random_status, '05 Dec 2012')


def test_create_request_success():
    request_result = request_dao.create_reimbursement_request(new_request)
    assert request_result.request_id != 0


def test_select_all_requests_by_employee_id():
    returned_employee_rr = request_dao.get_reimbursement_requests_by_id(2)
    assert len(returned_employee_rr) >= 2


def test_select_all_rr_success():
    rr = request_dao.get_all_reimbursement_history()
    assert len(rr) >= 1


def test_update_reimbursement_request():
    updated_rr = request_dao.update_reimbursement_request(update_rr)
    assert updated_rr.request_status == random_status


def test_get_pending_rr():
    pending_rr = request_dao.get_pending_reimbursement_requests()
    assert len(pending_rr) >= 3


def test_get_completed_rr():
    completed_rr = request_dao.get_pending_reimbursement_requests()
    assert len(completed_rr) >= 2
