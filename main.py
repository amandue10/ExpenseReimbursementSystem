# from flask import Flask, request, jsonify

# routes for application
# import logging
#
# logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")
from flask import Flask, jsonify

from data_access_layer.implementation_classes.employee_postgres_dao import EmployeePostgresDAO
from data_access_layer.implementation_classes.reimbursement_request_postgres_dao import ReimbursementRequestPostgresDAO
from entities import reimbursement_request
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


app.run()
