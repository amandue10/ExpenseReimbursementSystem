const header = document.createElement("h1");
header.textContent = `Welcome`;
document.body.appendChild(header);

const result = sessionStorage.getItem("value");

// for create employee rr ----
const reimbursementId = document.getElementById("reimbursementIdInput")
const employeeId = document.getElementById("employeeIdInput")
const managerId = document.getElementById("managerIdInput")
const requestAmount = document.getElementById("requestAmountInput")
const employeeComment = document.getElementById("employeeCommentInput")
const managerComment = document.getElementById("managerCommentInput")
const status = document.getElementById("statusBoxInput")
const requestDate = document.getElementById("requestDateInput")
// -----------------------------
const employeeTable = document.getElementById("employeeTable");
const employeeTableBody = document.getElementById("employeeTableBody");

function logout(){
    sessionStorage.clear();
    window.location.href = "login.html";
}


async function employeeCreateRequest(){
    let response = await fetch(
        "http://127.0.0.1:5000/reimbursement_request", {
            method:"POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"employeeId":employeeId.value, "managerId":managerId.value, "requestAmount":requestAmount.value, "requestComment":employeeComment.value,"requestComment2":managerComment.value, "requestId":reimbursementId.value, "requestStatus":status.value, "rrDate":requestDate.value })
        }
    )

    if (response.status === 200){
        document.location.reload(true)
        let body = await response.json()

     
    } else {
        alert("your Employee create request failed")
    }
}


async function getEmployeeData(){
    let url = "http://127.0.0.1:5000/reimbursement_requests/";

    let response = await fetch(url + result);
    
    if (response.status === 200){
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem trying to get the employee information: sorry!");
    }
}

function populateData(responseBody){
    
    

    for (let reimbursement_request of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement_request.employeeId}</td><td>${reimbursement_request.managerId}</td><td>${reimbursement_request.requestAmount}</td><td>${reimbursement_request.requestComment}</td><td>${reimbursement_request.requestComment2}</td><td>${reimbursement_request.requestStatus}<td>${reimbursement_request.rrDate}</td>`;
        employeeTableBody.appendChild(tableRow);
    }
}

getEmployeeData()