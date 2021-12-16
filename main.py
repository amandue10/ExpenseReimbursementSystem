# import logging
#
# logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")
from flask import Flask, jsonify, request

from data_access_layer.implementation_classes.employee_postgres_dao import EmployeePostgresDAO
from data_access_layer.implementation_classes.reimbursement_request_postgres_dao import ReimbursementRequestPostgresDAO
from entities import reimbursement_request
from entities.reimbursement_request import ReimbursementRequest
from service_layer.implementation_services.employee_postgres_service import EmployeePostgresService
from service_layer.implementation_services.reimbursement_request_postgres_service import \
    ReimbursementRequestPostgresService

app: Flask = Flask(__name__)

reimbursement_request_dao = ReimbursementRequestPostgresDAO()
reimbursement_request_service = ReimbursementRequestPostgresService(reimbursement_request_dao)


# employee_dao = EmployeePostgresDAO()
# employee_service = EmployeePostgresService(employee_dao)

# green pytest, pulls list in postman
# employee lists all rr's
@app.get("/reimbursement_requests/<employee_id>")
def get_employee_rrs_by_employee_id(employee_id: str):
    results = reimbursement_request_service.service_get_reimbursement_requests_by_id(int(employee_id))
    employee_rr_as_dictionaries = []
    for reimbursement_requests in results:
        rr_accounts_dictionaries = reimbursement_requests.make_rr_dictionary()
        employee_rr_as_dictionaries.append(rr_accounts_dictionaries)
        return jsonify(employee_rr_as_dictionaries), 200


# create rr
# green pytest, postman working and persisting to database
@app.post("/reimbursement_request")
def create_rr():
    body = request.get_json()
    new_rr = ReimbursementRequest(
        body["requestId"],
        body["employeeId"],
        body["managerId"],
        body["requestAmount"],
        body["requestComment"],
        body["requestComment2"],
        body["requestStatus"],
        body["rrDate"]
    )
    rr_to_return = reimbursement_request_service.service_create_reimbursement_request(new_rr)
    rr_as_dictionary = rr_to_return.make_rr_dictionary()
    rr_as_json = jsonify(rr_as_dictionary)
    return rr_as_json


# Pulls all pending requests.
# pytest green, postman working and pulling correct information
@app.get("/pending_requests")
def get_pending_requests():
    pending_requests = reimbursement_request_service.service_get_pending_reimbursement_requests()
    pending_requests_as_dictionary = []
    for reimbursement_request in pending_requests:
        dictionary_pending_request = reimbursement_request.make_rr_dictionary()
        pending_requests_as_dictionary.append(dictionary_pending_request)
    return jsonify(pending_requests_as_dictionary), 200


# Pulls all completed requests.
# pytest green, postman working and pulling correct information
@app.get("/completed_requests")
def get_completed_requests():
    completed_requests = reimbursement_request_service.service_get_completed_reimbursement_requests()
    completed_requests_as_dictionary = []
    for reimbursement_request in completed_requests:
        dictionary_completed_request = reimbursement_request.make_rr_dictionary()
        completed_requests_as_dictionary.append(dictionary_completed_request)
    return jsonify(completed_requests_as_dictionary)


@app.patch("/manager/request_decision/<request_id>")
def update_request(request_id: str):
    body = request.get_json()
    update_info = ReimbursementRequest(
        body["requestId"],
        body["employeeId"],
        body["managerId"],
        body["requestAmount"],
        body["requestComment"],
        body["requestComment2"],
        body["requestStatus"],
        body["rrDate"]
    )
    updated_rr = reimbursement_request_service.service_update_reimbursement_request(update_info)
    updated_rr_as_dictionary = updated_rr.make_rr_dictionary()
    return jsonify(updated_rr_as_dictionary), 200


app.run()
