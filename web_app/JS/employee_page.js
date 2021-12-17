const header = document.createElement("h1");
header.textContent = `Welcome`;
document.body.appendChild(header);

const result = sessionStorage.getItem("value");

// for create employee rr ----
const employeeId = document.getElementById("idInput")
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

// need to do constants for body to post
async function employeeCreateRequest(){
    let response = await fetch(
        "http://127.0.0.1:5000/reimbursement_request", {
            method:"POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"employeeId":employeeId.value, "managerId":managerId.value, "lastName":lastName.value, "password":password.value})
        }
    )
    if (response.status === 200){
        let body = await response.json()
        if (body["validated"]){
            sessionStorage.setItem("validated", true)
            window.location.href = "employee_page.html"
        } else {
            alert("Employee login failed: please try again")
        }
    } else {
        alert("your Employee login request failed")
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