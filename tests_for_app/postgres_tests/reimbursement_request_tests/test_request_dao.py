from data_access_layer.implementation_classes.reimbursement_request_postgres_dao import ReimbursementRequestPostgresDAO
from entities.reimbursement_request import ReimbursementRequest

request_dao = ReimbursementRequestPostgresDAO()

new_request = ReimbursementRequest(1, 1, 1, 200, "gas", " ", " ", '05 Dec 2000')


def test_create_request_success():
    request_result = request_dao.create_reimbursement_request(new_request)
    assert request_result.request_id != 0


def test_select_all_requests_by_employee_id():
    initial_request = request_dao.get_reimbursement_request_by_id(1)
    assert initial_request.employee_id == 1
